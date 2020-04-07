import os
import pandas as pd

# to_csv时，设置index=False 或 index=True，index_label = 'id'
# read_csv时，设置index_col=0即可

remain_game_id_path = '/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/final(6_q).csv'
games_features_path = '/Users/charles/PycharmProjects/Games_Research/add_ranking_company_age_colume/games-features(age).csv'

# max_period: 2018-07-01 to 2019-12-31
# max_count: 989


monthly_file_path = '/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/OUTPUT_DATA/Calendar_quarterly_csv/'
monthly_file_list = os.listdir(monthly_file_path)
monthly_file_list.sort()

# print(monthly_file_list[10:16])

monthly_file_list=monthly_file_list[10:16]
remain_game_id_df = pd.read_csv(remain_game_id_path)
games_features_df = pd.read_csv(games_features_path)
remain_games_features_df = pd.DataFrame(columns=games_features_df.columns.values)
count = 0
for index, row in remain_game_id_df.iterrows():
    double_match = games_features_df.loc[games_features_df['QueryID'] == row['ID']]
    if double_match.shape[0] == 1:
        remain_games_features_df = remain_games_features_df.append(double_match)
        count += 1


remain_games_features_df.to_csv('/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/test.csv')

for i in range(len(monthly_file_list)):
    month_data_df = pd.read_csv(monthly_file_path + monthly_file_list[i])
    colume_name='Owner_change_from '+monthly_file_list[i][0:24]
    id_sales_df = pd.DataFrame(columns=[colume_name])
    remain_games_features_df[colume_name] = id_sales_df[colume_name]

    for index, row in remain_games_features_df.iterrows():
        id_match = month_data_df.loc[month_data_df['ID'] == row['QueryID']]
        current_index = remain_games_features_df[remain_games_features_df['QueryID'] == row['QueryID']].index[0]
        print('ID:  '+ str(row['QueryID']))
        print('Current_index: '+ str(current_index))
        print('colume_name: '+ str(colume_name))
        print('Sales: '+ str(id_match))
        remain_games_features_df.loc[current_index, colume_name] = id_match['Sales'].iloc[0]

# # remain_games_features_df=remain_games_features_df.drop(['SupportURL'],axis=1)
# # remain_games_features_df=remain_games_features_df.drop(['SupportEmail'],axis=1)
# # remain_games_features_df=remain_games_features_df.drop(['AboutText'],axis=1)
# # remain_games_features_df=remain_games_features_df.drop(['ShortDescrip'],axis=1)
# # remain_games_features_df=remain_games_features_df.drop(['Background'],axis=1)
# # remain_games_features_df=remain_games_features_df.drop(['DetailedDescrip'],axis=1)
remain_games_features_df=remain_games_features_df.drop(['Unnamed: 0'],axis=1)
remain_games_features_df=remain_games_features_df.drop(['Unnamed: 0.1.1.1'],axis=1)
remain_games_features_df=remain_games_features_df.reset_index()
remain_games_features_df=remain_games_features_df.drop(['index'],axis=1)
print(remain_games_features_df.info())
remain_games_features_df.to_csv('/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/final(6_quarters).csv')
