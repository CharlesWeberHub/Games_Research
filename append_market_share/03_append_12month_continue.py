import os
import pandas as pd

all_id_name_path = '/Users/charles/PycharmProjects/Games_Research/data/monthly_data/steam_spy_id_name_list_from_html_table/all_id_name 2018-01-01 to 2020-01-26.html.csv'
remain_file_path = '/Users/charles/PycharmProjects/Games_Research/append_market_share/remain_games_name.csv'
games_features_path = '/Users/charles/PycharmProjects/Games_Research/append_market_share/games-features(age).csv'

monthly_file_path = '/Users/charles/PycharmProjects/Games_Research/data/original_monthly_data/'

monthly_file_list = os.listdir(monthly_file_path)
monthly_file_list.sort()

all_id_name_df = pd.read_csv(all_id_name_path)
remain_game_df=pd.read_csv(remain_file_path)
games_features_df = pd.read_csv(games_features_path)

print(type(games_features_df.columns.values))

remain_id_name_df = pd.DataFrame(columns=games_features_df.columns.values)
print(remain_id_name_df.info())

count=0
for index, row in remain_game_df.iterrows():
    result_match = all_id_name_df.loc[all_id_name_df['Name'] == row['Game']]
    if result_match.shape[0] == 1:
        double_match = games_features_df.loc[games_features_df['QueryID'] == result_match['ID'].iloc[0]]
        if double_match.shape[0] == 1:
            remain_id_name_df=remain_id_name_df.append(double_match)
            print(count)
            count += 1


for i in range(len(monthly_file_list)):
    month_data_df = pd.read_excel(monthly_file_path + monthly_file_list[i])
    id_name_df = pd.DataFrame(columns=['ID', 'Name'])
    for index, row in month_data_df.iterrows():
        result_match = all_id_name_df.loc[all_id_name_df['Name'] == row['Game']]

        if result_match.shape[0] == 1:
            double_match = remain_id_name_df.loc[remain_id_name_df['QueryID'] == result_match['ID'].iloc[0]]
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
    remain_id_name_df[colume_name] = id_sales_df[colume_name]

    for index, row in id_name_df.iterrows():
        # 得到匹配中的那一行，包含销售数据
        name_match = month_data_df.loc[month_data_df['Game'] == row['Name']]

        current_index = remain_id_name_df[remain_id_name_df['QueryID'] == row['ID']].index[0]

        remain_id_name_df.loc[current_index, colume_name] = name_match['Sales'].iloc[0]

remain_id_name_df.to_csv('/Users/charles/PycharmProjects/Games_Research/append_market_share/final(12_months).csv')
