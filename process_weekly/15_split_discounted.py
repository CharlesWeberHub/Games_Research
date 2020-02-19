import os
import pandas as pd

file_path = '/data/bi_weekly_data/merged_data/'
singlesheet_df = pd.read_csv(file_path + 'singlesheet_age.csv')[
    ['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
     'Userscore (Metascore)', 'Userscore', 'Metascore', 'Release date', 'RequiredAge', 'Developer(s)', 'Publisher(s)',
     'PlatformWindows', 'PlatformLinux',
     'PlatformMac', 'isMajorCompany','age']]


singlesheet_df['discounted_num']=singlesheet_df['Max discount'].str.split('%', 1).str[0]

singlesheet_df['discounted_num']=singlesheet_df['discounted_num'].fillna(0)
singlesheet_df['discounted_num']=singlesheet_df['discounted_num'].convert_objects(convert_numeric=True)
singlesheet_df['discounted']= singlesheet_df['discounted_num'] > 0

print(singlesheet_df.info())

singlesheet_df[['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount',
     'Userscore (Metascore)', 'Userscore', 'Metascore', 'Release date', 'RequiredAge', 'Developer(s)', 'Publisher(s)',
     'PlatformWindows', 'PlatformLinux',
     'PlatformMac', 'isMajorCompany', 'age','discounted']].to_csv(file_path + 'singlesheet_discounted.csv')