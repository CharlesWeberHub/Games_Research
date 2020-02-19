# generate all id and name

import os
import pandas as pd

file_path = '/Users/charles/PycharmProjects/Games_Research/data/biweekly/'

# The file that we need to merge
file_list = os.listdir(file_path)
file_list.sort()

# The time that is for us to analysis
time_period_list = []


def name_preparation():
    for file_name in file_list:
        period_str = file_name[16:27] + 'to ' + file_name[29:39]
        time_period_list.append(period_str)


# translate the name into id
def name_match_id():
    id_name_df = pd.DataFrame(columns=['ID', 'Name'])
    empty_name_df = pd.DataFrame(columns=['Name'])
    double_more_name_df = pd.DataFrame(columns=['Name'])
    df_idlist = pd.read_csv('All_id_name.csv')

    empty_result = 0
    double_or_more_match_count = 0
    repeated__original_items = 0
    sigle_match_count = 0
    total_original_items = 0

    for i in range(0, len(file_list)):

        df_steam_week = pd.read_excel(file_path + '/' + file_list[i])
        print(file_list[i])

        for index, row in df_steam_week.iterrows():

            result_match = df_idlist.loc[df_idlist['Name'] == row['Game']]

            if result_match.shape[0] == 0:
                empty_result += 1
                repeat_empty_name = empty_name_df.loc[empty_name_df['Name'] == row['Game']]
                if repeat_empty_name.shape[0] == 0:
                    empty_name_df = empty_name_df.append({'Name': row['Game']}, sort=True, ignore_index=True)
                continue

            if result_match.shape[0] > 1:
                double_or_more_match_count += 1
                repeat_double_more_name_df = double_more_name_df.loc[double_more_name_df['Name'] == row['Game']]
                if repeat_double_more_name_df.shape[0] == 0:
                    double_more_name_df = double_more_name_df.append({'Name': row['Game']}, sort=True,
                                                                     ignore_index=True)
                continue

            if result_match.shape[0] == 1:
                sigle_match_count += 1
                repeat_item = id_name_df.loc[id_name_df['Name'] == row['Game']]
                if repeat_item.shape[0] == 0:
                    id_name_df = id_name_df.append(result_match[['ID', 'Name']], sort=True, ignore_index=True)
                else:
                    repeated__original_items += 1

        print('Weekly Games: ' + str(df_steam_week.shape[0]))
        total_original_items += df_steam_week.shape[0]

    print('Empty Games by df:' + str(empty_name_df.shape[0]))
    print('double_or_more_match by df:' + str(double_more_name_df.shape[0]))
    print('Match Games by df: ' + str(id_name_df.shape[0]))

    print('Total_original_items by count:' + str(total_original_items))
    print('Empty Games by count:' + str(empty_result))
    print('double_or_more_match by count:' + str(double_or_more_match_count))
    print('sigle_match_count by count:' + str(sigle_match_count))

    id_name_df.to_csv('Match id_name.csv')


name_preparation()
name_match_id()

# data_set_df = pd.DataFrame(columns=time_period_list)
# print(time_period_list)
# data_set_df.to_csv('data_set.csv')
