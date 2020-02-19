import os
from datetime import datetime
import pandas as pd
from datetime import timedelta

file_path = '/Users/charles/PycharmProjects/Games_Research/data/merged_data/'

singlesheet_df = pd.read_csv(file_path + 'singlesheet.csv', low_memory=False)[
    ['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
     'Userscore (Metascore)', 'Userscore', 'Metascore', 'Release date', 'RequiredAge', 'Developer(s)', 'Publisher(s)',
     'PlatformWindows', 'PlatformLinux',
     'PlatformMac', 'isMajorCompany']]
#
#
# singlesheet_df['move_period']=period_list
# print(singlesheet_df)
# singlesheet_df['age']=singlesheet_df['age'].add(singlesheet_df['move_period'])
# print(singlesheet_df)


# print(singlesheet_df[['Release date']].shape)

start_day = datetime(2018, 12, 18)

singlesheet_df['days'] = start_day - pd.to_datetime(singlesheet_df['Release date'])
singlesheet_df.to_csv(file_path + 'singlesheet_days.csv')

singlesheet_df = pd.read_csv(file_path + 'singlesheet_days.csv', low_memory=False)[
    ['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
     'Userscore (Metascore)', 'Userscore', 'Metascore', 'Release date', 'RequiredAge', 'Developer(s)', 'Publisher(s)',
     'PlatformWindows', 'PlatformLinux',
     'PlatformMac', 'isMajorCompany', 'days']]

singlesheet_df['age'] = singlesheet_df['days'].str.split('days', 1).str[0]
singlesheet_df['age'] = singlesheet_df['age'].str.strip()

print(singlesheet_df['age'])
print(singlesheet_df.info())

singlesheet_df['one'] = 7
singlesheet_df['age'] = singlesheet_df['age'].astype('int').div(singlesheet_df['one'])
singlesheet_df['age'] = singlesheet_df['age'].astype('int') + 1


move_period = 0
for index in range(0, singlesheet_df.shape[0]):
    print(index)
    singlesheet_df.loc[index:index, 'age'] = int(singlesheet_df.loc[index:index, 'age'])+move_period
    move_period += 1
    if move_period == 6:
        move_period = 0

singlesheet_df[['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
     'Userscore (Metascore)', 'Userscore', 'Metascore', 'Release date', 'RequiredAge', 'Developer(s)', 'Publisher(s)',
     'PlatformWindows', 'PlatformLinux',
     'PlatformMac', 'isMajorCompany', 'age',]].to_csv(file_path + 'singlesheet_age.csv')
