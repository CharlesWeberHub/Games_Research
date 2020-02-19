# generate all id and name

import os
import pandas as pd

file_path = '/Users/charles/PycharmProjects/Games_Research/data/remain_games/remain_games_name.csv'


# translate the name into id
def name_match_id():
    id_name_df = pd.DataFrame(columns=['ID', 'Name'])
    empty_name_df = pd.DataFrame(columns=['Name'])
    double_more_name_df = pd.DataFrame(columns=['Name'])
    #df_idlist = pd.read_csv('/Users/charles/PycharmProjects/Games_Research/data/steam_spy_id_name_list/All_id_name.csv')
    df_idlist = pd.read_csv('/Users/charles/PycharmProjects/Games_Research/data/steam_spy_id_name_list/2018-12-18 to 2019-03-11 all_id_name.csv')

    empty_result = 0
    double_or_more_match_count = 0
    repeated__original_items = 0
    sigle_match_count = 0
    total_original_items = 0

    remain_games_name_df = pd.read_csv(file_path)

    for index, row in remain_games_name_df.iterrows():

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

    total_original_items += remain_games_name_df.shape[0]

    print('Empty Games by df:' + str(empty_name_df.shape[0]))
    print('double_or_more_match by df:' + str(double_more_name_df.shape[0]))
    print('Match Games by df: ' + str(id_name_df.shape[0]))

    print('Total_original_items by count:' + str(total_original_items))
    print('Empty Games by count:' + str(empty_result))
    print('double_or_more_match by count:' + str(double_or_more_match_count))
    print('sigle_match_count by count:' + str(sigle_match_count))

    id_name_df=id_name_df.sort_values(by='ID', ascending=True)
    id_name_df=id_name_df.reset_index()
    id_name_df[['ID','Name']].to_csv('/Users/charles/PycharmProjects/Games_Research/data/remain_games/remain_games_id_name_2018-12-18 to 2019-03-11.csv')

    print(empty_name_df)


name_match_id()
