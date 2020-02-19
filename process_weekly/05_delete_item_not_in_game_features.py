import os
import pandas as pd

game_features_file_path = '/data/bi_weekly_data/game_features(all_static_variables)/games-features.csv'
remain_games_id_name_file_path= '/data/bi_weekly_data/remain_games/remain_games_id_name_2018-12-18 to 2019-03-11(after_delete_not_in_yearly).csv'


id_name = pd.read_csv(remain_games_id_name_file_path)[['ID', 'Name']]
res_id_name = pd.read_csv(game_features_file_path)[['ResponseID', 'ResponseName']]

del_count = 0

print('delete_before: ' + str(id_name.shape[0]))

for index, row in id_name.iterrows():
    # find the id exits in the games-features.csv
    result_match = res_id_name.loc[res_id_name['ResponseID'] == row['ID']]
    if result_match.shape[0] < 1:
        # find the id no exits in the games-features.csv but exits in Match id_name.csv
        current_index = id_name.loc[id_name['ID'] == row['ID']].index.tolist()[0]
        # print(current_index)
        # delete the items in Match id_name.csv
        id_name = id_name.drop(index=current_index)
        del_count += 1

print('delete_after: ' + str(id_name.shape[0]))

print(del_count)

id_name.to_csv('/Users/charles/PycharmProjects/Games_Research/data/remain_games/remain_games_id_name_2018-12-18 to 2019-03-11(after_delete_not_in_game_features).csv')
