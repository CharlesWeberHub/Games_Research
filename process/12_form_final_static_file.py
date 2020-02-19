import os
import pandas as pd
import time
import re

file_path = '/Users/charles/PycharmProjects/Games_Research/data/biweekly(static_data_repeat)/'

game_size = 316
cut_game_index = 0

whole_single_df = pd.DataFrame(
    columns=['ID', 'Name', 'Release date', 'RequiredAge', 'Developer(s)', 'Publisher(s)', 'PlatformWindows',
             'PlatformLinux',
             'PlatformMac', 'isMajorCompany'])

while cut_game_index < game_size:
    print(cut_game_index)
    id_name = pd.read_csv(file_path + str(cut_game_index) + 'static.csv')
    whole_single_df = whole_single_df.append(id_name, sort=True, ignore_index=True)
    cut_game_index += 100

print(whole_single_df.shape)
whole_single_df.to_csv('/Users/charles/PycharmProjects/Games_Research/data/biweekly(static_data)/'+'final_repeat_static.csv')