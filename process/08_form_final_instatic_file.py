import os
import pandas as pd
import time
import re

file_path = '/Users/charles/PycharmProjects/Games_Research/data/biweekly(after_overlap)/'

# # The file that we need to merge
# file_list = os.listdir(file_path)
# file_list.sort()
# for file_name in file_list:
#     number = re.sub("\D", "", file_name)
#     print(number)
#     os.rename('/Users/charles/PycharmProjects/Simple_data/static_data/'+file_name, '/Users/charles/PycharmProjects/Simple_data/static_data/'+str(number)+'.csv')
#
file_list = os.listdir(file_path)

whole_single_df = pd.DataFrame(
    columns=['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
             'Userscore (Metascore)'])

for i in range(0, len(file_list)):
    id_name = pd.read_csv(file_path + file_list[i])
    whole_single_df = whole_single_df.append(id_name, sort=True, ignore_index=True)

whole_single_df=whole_single_df[['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
                 'Userscore (Metascore)']]


time_period = []
periods = 6
for file_id in range(1, periods + 1):
    time_period.append(int(file_id))


row_size = whole_single_df.shape[0]
row_index = 0
while row_index < row_size - 1:
    whole_single_df.iloc[row_index:row_index + periods, 2:3] = time_period
    row_index += periods

whole_single_df['Time_period']=whole_single_df['Time_period'].astype("int")
whole_single_df[['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
                 'Userscore (Metascore)']].to_csv(
    '/Users/charles/PycharmProjects/Games_Research/data/biweekly(singlesheet_instatic_plus_time_period)/' + 'singlesheet_instatic.csv')

