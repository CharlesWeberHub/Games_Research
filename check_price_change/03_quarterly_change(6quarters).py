import pandas as pd
import os
import copy

remain_id_file_path = '/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/final(6_q).csv'

remain_id_df=pd.read_csv(remain_id_file_path)

monthly_data_df=pd.read_csv('/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/OUTPUT_DATA/Calendar_quarterly_csv/2016-01-01 to 2016-03-31 (quarterly_data).csv',index_col=0)

print(monthly_data_df.columns.values)
monthly_data_features_df = pd.DataFrame(columns=monthly_data_df.columns.values)

monthly_file_path = '/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/OUTPUT_DATA/Calendar_quarterly_csv/'
monthly_file_list = os.listdir(monthly_file_path)
monthly_file_list.sort()
monthly_file_list=monthly_file_list[10:16]

for index,row in remain_id_df.iterrows():
    id=row['ID']
    print(id)
    for i in range(len(monthly_file_list)):
        month_data_df = pd.read_csv(monthly_file_path + monthly_file_list[i])
        monthly_data_features_df=monthly_data_features_df.append(month_data_df[month_data_df['ID']==id], sort=True, ignore_index=True)

monthly_data_features_df=monthly_data_features_df.drop(["Unnamed: 0"],axis=1)
monthly_data_features_df=monthly_data_features_df.reset_index()
monthly_data_features_df=monthly_data_features_df.drop(["index"],axis=1)

monthly_data_features_df.to_csv('/Users/charles/PycharmProjects/Games_Research/check_price_change/merge_6_quarter.csv')