import os
import re

import pandas as pd

singlesheet_df = \
    pd.read_csv('/Users/charles/PycharmProjects/Games_Research/data/merged_data/singlesheet_discounted.csv')[
        ['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
         'Userscore (Metascore)', 'Userscore', 'Metascore', 'Release date', 'RequiredAge', 'Developer(s)',
         'Publisher(s)',
         'PlatformWindows', 'PlatformLinux',
         'PlatformMac', 'isMajorCompany', 'age', 'discounted']]

group_df = singlesheet_df[['ID', 'Owners after']].groupby("ID").describe()
group_df['max_owner'] = group_df.iloc[:, 7:8]

group_df.to_csv('/Users/charles/PycharmProjects/Games_Research/data/group_results/' + 'result.csv')
group_df = pd.read_csv('/Users/charles/PycharmProjects/Games_Research/data/group_results/' + 'result.csv').drop(
    [0, 1]).reset_index(drop=True)
group_df = group_df.sort_values(by='max_owner', ascending=False)
print(group_df.columns)
id_max = pd.DataFrame()
group_df = group_df.rename(columns={'Unnamed: 0': 'ID'})
id_max['ID'] = group_df['ID']
id_max['max_owner'] = group_df['max_owner']
id_max['low_owner'] = True
id_max.loc[id_max['max_owner'] > id_max['max_owner'][int(id_max.shape[0] * 0.2)], 'low_owner'] = False
id_max = id_max.convert_objects(convert_numeric=True)
id_max = id_max.sort_values(by='ID', ascending=True)
print(id_max)

Low_bool_list = []
game_now_index = 0
move_period = 0

for index in range(0, singlesheet_df.shape[0]):
    Low_bool_list.append(id_max['low_owner'][game_now_index])
    move_period += 1
    if move_period == 6:
        move_period = 0
        game_now_index += 1

singlesheet_df['low_owner'] = Low_bool_list
singlesheet_df[['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
                'Userscore (Metascore)', 'Userscore', 'Metascore', 'Release date', 'RequiredAge', 'Developer(s)',
                'Publisher(s)',
                'PlatformWindows', 'PlatformLinux',
                'PlatformMac', 'isMajorCompany', 'age', 'low_owner']].to_csv(
    '/Users/charles/PycharmProjects/Games_Research/data/merged_data/singlesheet_low_owner.csv')
