import os
import pandas as pd
import time

file_path = '/data/bi_weekly_data/biweekly(after filter)/'

# The file that we need to merge
file_list = os.listdir(file_path)
file_list.sort()

whole_df = pd.DataFrame(
    columns=['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
             'Userscore (Metascore)'])
game_size = 316

week_list_df = []

merge_list = []

cut_game_index = 0

for i in range(0, len(file_list)):
    week_list_df.append(pd.read_csv(file_path + file_list[i]))

file_id = 1
while cut_game_index < game_size:
    # print(cut_game_index)
    start = time.time()
    whole_single_df = pd.DataFrame(
        columns=['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
                 'Userscore (Metascore)'])

    if cut_game_index == 300:
        for index in range(cut_game_index, cut_game_index + 16):
            for i in range(0, len(file_list)):
                df_steam_week = week_list_df[i]
                this_game_week_data = df_steam_week.iloc[index,]
                whole_single_df = whole_single_df.append(this_game_week_data)

        whole_single_df.to_csv('/Users/charles/PycharmProjects/Games_Research/data/biweekly(after_overlap)/' + str(file_id) + 'static.csv')
        print(str(file_id))
        end = time.time()
        print("Run_Cost:%.2f Second" % (end - start))
        file_id += 1
        cut_game_index += 60

    else:
        for index in range(cut_game_index, cut_game_index + 100):
            for i in range(0, len(file_list)):
                df_steam_week = week_list_df[i]
                this_game_week_data = df_steam_week.iloc[index,]
                whole_single_df = whole_single_df.append(this_game_week_data)

        whole_single_df.to_csv('/Users/charles/PycharmProjects/Games_Research/data/biweekly(after_overlap)/' + str(file_id) + 'static.csv')
        print(str(file_id))
        end = time.time()
        print("Run_Cost:%.2f Second" % (end - start))
        file_id += 1
        cut_game_index += 100
else:
    print(cut_game_index)
    print('finish')


