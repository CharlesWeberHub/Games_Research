import os
import pandas as pd

all_steam_year = pd.read_csv('/data/bi_weekly_data/yearly_data_for_static_variable/merge_yearly_data.csv')
res_id_name = pd.read_csv('/data/bi_weekly_data/game_features(all_static_variables)/games-features.csv')
id_name = pd.read_csv(
    '/data/bi_weekly_data/remain_games/remain_games_id_name_2018-12-18 to 2019-03-11(after_delete_not_in_game_features).csv')[['ID', 'Name']]
sta_data_df = pd.DataFrame(
    columns=['ID', 'Name', 'Release date','RequiredAge','Developer(s)', 'Publisher(s)', 'PlatformWindows', 'PlatformLinux',
             'PlatformMac'])
sta_data_df[['ID', 'Name']] = id_name

for index, row in all_steam_year.iterrows():
    result_match = sta_data_df.loc[sta_data_df['Name'] == row['Game']]
    if result_match.shape[0] == 1:
        current_index = result_match.index.tolist()[0]
        sta_data_df.loc[current_index, ['Release date', 'Developer(s)', 'Publisher(s)']] = [
            row['Release date'], row['Developer(s)'], row['Publisher(s)']]

for index, row in res_id_name.iterrows():
    result_match = sta_data_df.loc[sta_data_df['ID'] == row['ResponseID']]
    if result_match.shape[0] == 1:
        current_index = result_match.index.tolist()[0]
        sta_data_df.loc[current_index, ['RequiredAge','PlatformWindows','PlatformLinux', 'PlatformMac']] = [
            row['RequiredAge'],row['PlatformWindows'], row['PlatformLinux'], row['PlatformMac']]

sta_data_df.to_csv('/Users/charles/PycharmProjects/Games_Research/data/biweekly(static_data)/static.csv')
print('hello')
