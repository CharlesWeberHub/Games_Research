import os
import pandas as pd
import time
import re

whole_single_df = pd.read_csv(
    '/Users/charles/PycharmProjects/Games_Research/data/monthly_data/monthly(singlesheet_instatic_plus_time_period)/singlesheet_instatic.csv')[['ID', 'Name', 'Time_period', 'Owners before', 'Owners after', 'Sales', 'Price', 'Max discount', 'Userscore (Metascore)']]
whole_single_df['Userscore']=whole_single_df['Userscore (Metascore)'].str.split('(', 1).str[0]
whole_single_df['Metascore']=whole_single_df['Userscore (Metascore)'].str.split('(', 1).str[1]
whole_single_df['Metascore']=whole_single_df['Metascore'].str.split(')', 1).str[0]
whole_single_df['Userscore']=whole_single_df['Userscore'].str.strip()
whole_single_df['Metascore']=whole_single_df['Metascore'].str.strip()

whole_single_df.to_csv('/Users/charles/PycharmProjects/Games_Research/data/monthly_data/monthly(split_score)/' + 'singlesheet_instatic_plus_time_period_split_score.csv')


static_data_df = pd.read_csv('/Users/charles/PycharmProjects/Games_Research/data/monthly_data/monthly(static_data)/static.csv')
print(static_data_df.info())

major_company_file_path = '/Users/charles/PycharmProjects/Games_Research/data/monthly_data/major_company/'

major_company = pd.read_csv(major_company_file_path + 'MajorCompany.csv')

company_list=pd.concat(major_company.iloc[:,i] for i in range(1,major_company.shape[1]))
company_list.index=pd.np.arange(len(company_list))
company_list=company_list.dropna().unique().tolist()
print(type(company_list))
print(len(company_list))
print(company_list)


def string_finder(columns, words):
    if any(word in field for field in columns for word in words):
        return True
    return False


static_data_df['isMajorCompany'] = static_data_df[['Publisher(s)']].astype(str).apply(string_finder,
                                                                                      words=company_list, axis=1)
print(static_data_df.info())

static_data_df[['ID', 'Name', 'Release date','RequiredAge', 'Developer(s)', 'Publisher(s)', 'PlatformWindows', 'PlatformLinux',
                'PlatformMac', 'isMajorCompany']].to_csv('/Users/charles/PycharmProjects/Games_Research/data/monthly_data/monthly(static_data)/static_plus_major_company.csv')



