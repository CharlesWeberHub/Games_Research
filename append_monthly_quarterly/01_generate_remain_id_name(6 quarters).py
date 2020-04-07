import pandas as pd
import os
import copy

monthly_data_path = '/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/OUTPUT_DATA/Calendar_quarterly_csv/'
#game_features_path = '/Users/charles/PycharmProjects/Games_Research/data/game_feature/games-features(40604 rows).csv'
game_features_path = '/Users/charles/PycharmProjects/Games_Research/add_ranking_company_age_colume/games-features(age).csv'

monthly_data_file_list = os.listdir(monthly_data_path)
monthly_data_file_list.sort()

game_id_set = set()

max_period = ''
max_count = 0
game_id_list_max=list()

game_features_df = pd.read_csv(game_features_path)

for i in range(len(monthly_data_file_list)):

    if 6 + i > len(monthly_data_file_list):
        break

    period = monthly_data_file_list[0 + i][0:13] + monthly_data_file_list[5 + i][13:24]

    game_id_list = {}
    for i, file in enumerate(monthly_data_file_list[0 + i:6 + i]):
        if i == 0:
            game_id_list = pd.read_csv(monthly_data_path + file)['ID'].tolist()
            game_id_set = set(game_id_list)
        else:
            game_id_list = pd.read_csv(monthly_data_path + file)['ID'].tolist()
            current_game_set = set(game_id_list)
            game_id_set = game_id_set & current_game_set

    game_id_set_copy = copy.copy(game_id_set)

    for index, value in enumerate(game_id_set_copy):
        id_match = game_features_df.loc[game_features_df['QueryID'] == value]
        if id_match.shape[0] != 1:
            game_id_set.remove(value)

    set_len = len(game_id_set)

    if set_len > max_count:
        max_period = period
        max_count = set_len
        game_id_list_max=list(game_id_set)

    print(period+'  -------  remain_games:'+ str(set_len))

print('max_period: ' + str(max_period))
print('max_count: ' + str(max_count))

name=['ID']
game_id_list_max_df=pd.DataFrame(columns=name,data=game_id_list_max)
game_id_list_max_df.to_csv('/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/final(6_q).csv')


