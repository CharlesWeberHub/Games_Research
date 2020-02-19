import os
import pandas as pd
import time
import re

whole_single_df = pd.read_csv(
    '/data/bi_weekly_data/biweekly(split_score)/singlesheet_instatic_plus_time_period_split_score.csv')
whole_static_df = pd.read_csv('/data/bi_weekly_data/biweekly(static_data)/final_repeat_static.csv')

print(whole_single_df.info())
print(whole_static_df.info())

df1 = whole_single_df[['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
                       'Userscore (Metascore)','Userscore','Metascore']]
df2 = whole_static_df[['ID', 'Release date', 'RequiredAge', 'Developer(s)', 'Publisher(s)', 'PlatformWindows',
                       'PlatformLinux',
                       'PlatformMac', 'isMajorCompany']]

df1[['Release date', 'RequiredAge', 'Developer(s)', 'Publisher(s)', 'PlatformWindows', 'PlatformLinux', 'PlatformMac','isMajorCompany']] = df2.iloc[:, 1:]

print(df1.info())

df1.to_csv('/Users/charles/PycharmProjects/Games_Research/data/merged_data/'+'singlesheet.csv')
