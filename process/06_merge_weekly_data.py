# Merge weekly data

import os
import pandas as pd

file_path = '/Users/charles/PycharmProjects/Games_Research/data/biweekly'

# The file that we need to merge
file_list = os.listdir(file_path)
file_list.sort()

# The time that is for us to analysis
time_period_list = []

id_name = pd.read_csv('/Users/charles/PycharmProjects/Games_Research/data/remain_games/remain_games_id_name_2018-12-18 to 2019-03-11(after_delete_not_in_game_features).csv')[['ID', 'Name']]


def name_preparation():
    for file_name in file_list:
        period_str = file_name[16:27] + 'to ' + file_name[29:39]
        time_period_list.append(period_str)


def create_frame_file():
    for i in range(0, len(file_list)):

        df_steam_week = pd.read_csv(file_path + '/' + file_list[i])
        print(file_list[i])
        weekly_data_df = pd.DataFrame(columns=['ID', 'Name','Owners before','Owners after','Sales', 'Price', 'Max discount', 'Userscore (Metascore)'])
        weekly_data_df[['ID', 'Name']] = id_name
        for index, row in df_steam_week.iterrows():
            result_match = weekly_data_df.loc[weekly_data_df['Name'] == row['Game']]
            if result_match.shape[0] == 1:
                current_index = weekly_data_df[weekly_data_df['Name'] == row['Game']].index.tolist()[0]
                weekly_data_df.loc[current_index, ['Owners before','Owners after','Sales', 'Price', 'Max discount', 'Userscore (Metascore)']] = [
                    row['Owners before'], row['Owners after'],row['Sales'], row['Price'], row['Max discount'], row['Userscore (Metascore)']]

        weekly_data_df.to_csv(
            '/Users/charles/PycharmProjects/Games_Research/data/biweekly(after filter)/' + str(time_period_list[i]) + '.csv')
        print('hello')


name_preparation()
create_frame_file()
