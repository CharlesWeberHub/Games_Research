import os
import pandas as pd
import time
import re

file_path = '/Users/charles/PycharmProjects/Games_Research/data/merged_data/'
singlesheet_df = pd.read_csv(file_path + 'singlesheet_age.csv')[
    ['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
     'Userscore (Metascore)', 'Userscore', 'Metascore', 'Release date', 'RequiredAge', 'Developer(s)', 'Publisher(s)',
     'PlatformWindows', 'PlatformLinux',
     'PlatformMac', 'isMajorCompany','age']]

#singlesheet_df=singlesheet_df.convert_objects(convert_numeric=True)
print(singlesheet_df.info())

#print(type(singlesheet_df.groupby("ID").describe()))
# group_df=singlesheet_df.groupby("ID").describe()
# group_df.to_csv('temp.csv')
# print(group_df)
# print(group_df[['ID','Owners after.7']])
#
#
# search_res_df['id'] = search_res_df.iloc[:, 0:1]
# search_res_df['max_owner'] = search_res_df.iloc[:, 7:8]
# # print(search_res_df['max_owner'].dtypes)
# # search_res_df['max_owner'] = int(search_res_df['max_owner'])
# search_res_df = search_res_df.drop([0, 1]).reset_index(drop=True)
#
# # search_res_df=search_res_df.sort_values(by='max_owner',ascending=False)
#
# # print(search_res_df[['id', 'max_owner']])
#
#
# id_max = pd.DataFrame()
# id_max['ID'] = search_res_df['id']
# id_max['max_owner'] = search_res_df['max_owner']
#
#
# id_max = id_max.convert_objects(convert_numeric=True)
#
#
# id_max=id_max.sort_values(by='max_owner',ascending=False)
# id_max['lowowner']=True
# id_max['lowowner'][0:2239]=False
#
# print(id_max)
#
# id_max[['ID', 'max_owner', 'lowowner']].to_csv('/Users/charles/PycharmProjects/Simple_data/total_data/lowowner.csv')

# singlesheet_df = pd.read_csv('/Users/charles/PycharmProjects/Simple_data/total_data/singlesheet.csv', low_memory=False)
#
# singlesheet_df = singlesheet_df.rename(columns={'Unnamed: 0': 'ord'})
#
# singlesheet_df = singlesheet_df.sort_values(by='ID', ascending=True)
# singlesheet_df.to_csv('/Users/charles/PycharmProjects/Simple_data/total_data/singlesheet_id.csv')

# id_max_df = pd.read_csv('/Users/charles/PycharmProjects/Simple_data/total_data/lowowner.csv', low_memory=False)
# id_max_df = id_max_df.sort_values(by='ID', ascending=True)
# id_max_df = id_max_df.reset_index()
# print(id_max_df.head())
# # id_max_df.to_csv('/Users/charles/PycharmProjects/Simple_data/total_data/lowowner_id.csv')
#
#
# Low_bool_list = []
# game_now_index = 0
# move_period = 0
#
# print(id_max_df[id_max_df['ID']==578080])
#
# for index in range(0, 602640):
#     Low_bool_list.append(id_max_df['lowowner'][game_now_index])
#     move_period += 1
#     if move_period == 54:
#         move_period = 0
#         game_now_index += 1
#
# print(Low_bool_list[410944])

# singlesheet_id_df = pd.read_csv('/Users/charles/PycharmProjects/Simple_data/total_data/singlesheet_id.csv',
#                                 low_memory=False)
# singlesheet_id_df['low_owner'] = Low_bool_list
#
# print(singlesheet_id_df[singlesheet_id_df['ID'] == 578080])
#
# singlesheet_id_df = singlesheet_id_df.sort_values(by='ord', ascending=True)

# singlesheet_id_df.to_csv('/Users/charles/PycharmProjects/Simple_data/total_data/singlesheet_ord_id.csv')

# singlesheet_df = pd.read_csv('/Users/charles/PycharmProjects/Simple_data/total_data/singlesheet_ord_id.csv', low_memory=False)[
#     ['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
#      'Userscore (Metascore)', 'Userscore', 'Metascore', 'Release date', 'RequiredAge', 'Developer(s)', 'Publisher(s)',
#      'PlatformWindows', 'PlatformLinux',
#      'PlatformMac', 'isMajorCompany', 'age','isRetro','low_owner']]
#
# singlesheet_df.to_csv('/Users/charles/PycharmProjects/Simple_data/total_data/singlesheet.csv')