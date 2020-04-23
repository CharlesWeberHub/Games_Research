import pandas as pd
import os
import copy

monthly_data_path = '/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/OUTPUT_DATA/Calendar_monthly_csv/'
monthly_data_file_list = os.listdir(monthly_data_path)
monthly_data_file_list.sort()

genre_file_path = '/Users/charles/PycharmProjects/Games_Research/IV_append/genre_excel/'
genre_data_file_list = os.listdir(genre_file_path)
genre_data_file_list.sort()

games_features_path = '/Users/charles/PycharmProjects/Games_Research/add_ranking_company_age_colume/games-features(age_month6).csv'

genre_list = ['Action', 'Adventure', 'Early+Access', 'Ex+Early+Access', 'Free', 'Indie', 'Massively', 'RPG',
              'Simulation', 'Sports', 'Strategy', 'Others']

games_features_df = pd.read_csv(games_features_path, index_col=0)

# max_period: 2017-04-01 to 2017-09-30
# max_count: 666

monthly_data_file_list = monthly_data_file_list[15:21]

# store the whole genre data
genre_list_dic = {}

# the statistic of these months data
genre_statis_dic = {}

id_genre_statis_df = pd.DataFrame(columns=genre_list)

for i, _genre_file in enumerate(genre_data_file_list):
    genre_data_df = pd.read_csv(genre_file_path + _genre_file, index_col=0)['ID']
    id_list = genre_data_df.tolist()
    id_set = set(id_list)
    genre_list_dic[genre_list[i]] = id_set

for i, month_data in enumerate(monthly_data_file_list):

    for i, _genre_tag in enumerate(genre_list):
        genre_statis_dic[genre_list[i]] = 0

    month_data_df = pd.read_csv(monthly_data_path + month_data, index_col=0)[['ID', 'Game']]

    repeat_count = 0

    for index, row in month_data_df.iterrows():

        has_genre_count = 0
        double_match = games_features_df.loc[games_features_df['QueryID'] == row['ID']]
        if double_match.shape[0] != 1:
            print(row['ID'])

        for key in genre_list_dic.keys():

            if row['ID'] in genre_list_dic[key]:
                # print(key)
                c_count = genre_statis_dic[key]
                c_count = c_count + 1
                genre_statis_dic[key] = c_count
                has_genre_count += 1

        if has_genre_count != 0:
            repeat_count = repeat_count + has_genre_count - 1
        else:
            c_count = genre_statis_dic['Others']
            c_count = c_count + 1
            genre_statis_dic['Others'] = c_count

    id_genre_statis_df = id_genre_statis_df.append(
        [{'Action': genre_statis_dic['Action'], 'Adventure': genre_statis_dic['Adventure'],
          'Early+Access': genre_statis_dic['Early+Access'], 'Ex+Early+Access': genre_statis_dic['Ex+Early+Access'],
          'Free': genre_statis_dic['Free'], 'Indie': genre_statis_dic['Indie'],
          'Massively': genre_statis_dic['Massively'], 'RPG': genre_statis_dic['RPG'],
          'Simulation': genre_statis_dic['Simulation'], 'Sports': genre_statis_dic['Sports'],
          'Strategy': genre_statis_dic['Strategy'], 'Others': genre_statis_dic['Others']}], ignore_index=True)

id_genre_statis_df.to_csv(
    '/Users/charles/PycharmProjects/Games_Research/IV_append/genre_mean_age_append_iv/' + 'genre_statis_mean_age(6 months).csv')
print(id_genre_statis_df)
