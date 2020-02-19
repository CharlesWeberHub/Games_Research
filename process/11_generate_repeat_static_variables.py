import os
import pandas as pd
import time

static_data_df = pd.read_csv('/Users/charles/PycharmProjects/Games_Research/data/biweekly(static_data)/static_plus_major_company.csv')[
    ['ID', 'Name', 'Release date', 'RequiredAge', 'Developer(s)', 'Publisher(s)', 'PlatformWindows', 'PlatformLinux',
     'PlatformMac', 'isMajorCompany']]

# repeat_static_df = pd.DataFrame(
#     columns=['ID', 'Name', 'Release date', 'RequiredAge', 'Developer(s)', 'Publisher(s)', 'PlatformWindows',
#              'PlatformLinux',
#              'PlatformMac', 'isMajorCompany', 'isRetro'])
#
# for row in range(0,11160):
#     print(row)
#     for index in range(0,54):
#         repeat_static_df=repeat_static_df.append(static_data_df.loc[0,:])

game_size = static_data_df.shape[0]
cut_game_index = 0
periods=6

output_file_path='/Users/charles/PycharmProjects/Games_Research/data/biweekly(static_data_repeat)/'

while cut_game_index < game_size:
    # print(cut_game_index)
    start = time.time()
    repeat_static_df = pd.DataFrame(
        columns=['ID', 'Name', 'Release date', 'RequiredAge', 'Developer(s)', 'Publisher(s)', 'PlatformWindows',
                 'PlatformLinux',
                 'PlatformMac', 'isMajorCompany'])

    if cut_game_index == 300:
        for index in range(cut_game_index, cut_game_index + 16):
            for i in range(0, periods):
                repeat_static_df = repeat_static_df.append(static_data_df.loc[index, :])
        repeat_static_df.to_csv(output_file_path + str(cut_game_index) + 'static.csv')

        end = time.time()
        print("Run_Cost:%.2f Second" % (end - start))
        cut_game_index += 60

    else:
        for index in range(cut_game_index, cut_game_index + 100):
            for i in range(0, periods):
                repeat_static_df = repeat_static_df.append(static_data_df.loc[index, :])

        repeat_static_df.to_csv(output_file_path + str(cut_game_index) + 'static.csv')

        end = time.time()
        print("Run_Cost:%.2f Second" % (end - start))
        cut_game_index += 100
else:
    print(cut_game_index)
    print('finish')


print(repeat_static_df)