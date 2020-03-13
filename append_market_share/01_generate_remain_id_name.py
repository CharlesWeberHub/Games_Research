import os
import pandas as pd

all_id_name_path = '/Users/charles/PycharmProjects/Games_Research/data/monthly_data/steam_spy_id_name_list_from_html_table/all_id_name 2018-01-01 to 2020-01-26.html.csv'
monthly_file_path = '/Users/charles/PycharmProjects/Games_Research/data/original_monthly_data/'
result_game_path = '/Users/charles/PycharmProjects/Games_Research/append_market_share/gamedata.csv'

monthly_file_list = os.listdir(monthly_file_path)
monthly_file_list.sort()

all_id_name_df = pd.read_csv(all_id_name_path)
result_game_df = pd.read_csv(result_game_path)

for i in range(len(monthly_file_list)):
    month_data_df = pd.read_excel(monthly_file_path + monthly_file_list[i])
    id_name_df = pd.DataFrame(columns=['ID', 'Name'])
    for index, row in month_data_df.iterrows():
        result_match = all_id_name_df.loc[all_id_name_df['Name'] == row['Game']]

        if result_match.shape[0] == 1:
            double_match = result_game_df.loc[result_game_df['QueryID'] == result_match['ID'].iloc[0]]
            if double_match.shape[0] !=1:
                continue

            repeat_item = id_name_df.loc[id_name_df['Name'] == row['Game']]
            if repeat_item.shape[0] == 0:
                id_name_df = id_name_df.append(result_match[['ID', 'Name']], sort=True, ignore_index=True)
            else:
                print('repeat')
    colume_name='Owner_change_from '+monthly_file_list[i][16:39]
    print(colume_name)
    id_sales_df = pd.DataFrame(columns=[colume_name])
    result_game_df[colume_name] = id_sales_df[colume_name]

    for index, row in id_name_df.iterrows():
        # 得到匹配中的那一行，包含销售数据
        name_match = month_data_df.loc[month_data_df['Game'] == row['Name']]

        current_index = result_game_df[result_game_df['QueryID'] == row['ID']].index[0]

        result_game_df.loc[current_index, colume_name] = name_match['Sales'].iloc[0]

result_game_df.to_csv('/Users/charles/PycharmProjects/Games_Research/append_market_share/final.csv')

#
# all_id_name_df = pd.read_csv(all_id_name_path)
# month_data_df = pd.read_excel(monthly_file_path)
# result_game_df = pd.read_csv(result_game_path)
#
# id_name_df = pd.DataFrame(columns=['ID', 'Name'])
#
# for index, row in month_data_df.iterrows():
#     result_match = all_id_name_df.loc[all_id_name_df['Name'] == row['Game']]
#
#     if result_match.shape[0] == 1:
#         double_match = result_game_df.loc[result_game_df['QueryID'] == result_match['ID'].iloc[0]]
#         if double_match.shape[0] !=1:
#             continue
#
#         repeat_item = id_name_df.loc[id_name_df['Name'] == row['Game']]
#         if repeat_item.shape[0] == 0:
#             id_name_df = id_name_df.append(result_match[['ID', 'Name']], sort=True, ignore_index=True)
#         else:
#             print('repeat')
#
# print(id_name_df.info())
# id_name_df.to_csv('/Users/charles/PycharmProjects/Games_Research/append_market_share/temp_id_name.csv')
#
