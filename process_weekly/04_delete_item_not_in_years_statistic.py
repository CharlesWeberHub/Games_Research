# generate the variable that unchanged

import os
import pandas as pd

years_file_path = '/data/bi_weekly_data/yearly_data_for_static_variable/merge_yearly_data.csv'
remain_games_id_name_file_path= '/data/bi_weekly_data/remain_games/remain_games_id_name_2018-12-18 to 2019-03-11.csv'

yearly_data_df=pd.read_csv(years_file_path)
id_name = pd.read_csv(remain_games_id_name_file_path)[['ID', 'Name']]

del_count = 0

for index, row in id_name.iterrows():
    # find the id exits in the Years_data
    result_match = yearly_data_df.loc[yearly_data_df['Game'] == row['Name']]

    if result_match.shape[0] == 1:
        continue

    else:
        current_index = id_name.loc[id_name['Name'] == row['Name']].index.tolist()[0]
        id_name = id_name.drop(index=current_index)
        del_count += 1

print(del_count)
id_name=id_name.reset_index()
id_name.to_csv('/Users/charles/PycharmProjects/Games_Research/data/remain_games/remain_games_id_name_2018-12-18 to 2019-03-11(after_delete_not_in_yearly).csv')
