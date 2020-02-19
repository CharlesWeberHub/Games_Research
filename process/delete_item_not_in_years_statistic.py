# generate the variable that unchanged

import os
import pandas as pd

years_file_path = '/Users/charles/Desktop/Compress/Years_data/'

id_name = pd.read_csv('Match id_name.csv')[['ID', 'Name']]

yearly_data_df=pd.read_csv('merge_yearly_data.csv')

# df_year2018 = \
#     pd.read_csv(years_file_path + '2018 - Year Stats - SteamSpy - All the data and stats about Steam games.csv')[
#         ['Game', 'Release date', 'Developer(s)', 'Publisher(s)']]
#
# df_year2019 = \
#     pd.read_csv(years_file_path + '2019 - Year Stats - SteamSpy - All the data and stats about Steam games.csv')[
#         ['Game', 'Release date', 'Developer(s)', 'Publisher(s)']]

del_count = 0

for index, row in id_name.iterrows():
    # find the id exits in the Years_data
    result_match = yearly_data_df.loc[yearly_data_df['Game'] == row['Name']]

    if result_match.shape[0] == 1:
        continue

    else:
        current_index = id_name.loc[id_name['Name'] == row['Name']].index.tolist()[0]
        id_name = id_name.drop(index=current_index)
        del_count += 1

print(del_count)
id_name.to_csv('Match id_name.csv')
