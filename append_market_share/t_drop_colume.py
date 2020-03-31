import os
import pandas as pd

remain_id_name_df=pd.read_csv('/Users/charles/PycharmProjects/Games_Research/append_market_share/final(12_months).csv')
# remain_id_name_df=remain_id_name_df.drop(['Unnamed: 0'],axis=1)
# remain_id_name_df=remain_id_name_df.drop(['SupportURL'],axis=1)
# remain_id_name_df=remain_id_name_df.drop(['SupportEmail'],axis=1)
# remain_id_name_df=remain_id_name_df.drop(['AboutText'],axis=1)
#remain_id_name_df=remain_id_name_df.drop(['ShortDescrip','DetailedDescrip','Background'],axis=1)
#remain_id_name_df=remain_id_name_df.drop(['Background'],axis=1)
# remain_id_name_df=remain_id_name_df.drop(['Unnamed: 0.1.1.1.1.1'],axis=1)
# remain_id_name_df=remain_id_name_df.drop(['Unnamed: 0.1.1.1.1'],axis=1)
# remain_id_name_df=remain_id_name_df.drop(['Unnamed: 0.1.1.1'],axis=1)
# remain_id_name_df=remain_id_name_df.drop(['Unnamed: 0.1.1'],axis=1)
# remain_id_name_df=remain_id_name_df.drop(['Unnamed: 0.1'],axis=1)
# remain_id_name_df=remain_id_name_df.drop(['Unnamed: 0'],axis=1)
remain_id_name_df=remain_id_name_df.drop(['Unnamed: 0.1'],axis=1)

print(remain_id_name_df.info())
remain_id_name_df.to_csv('/Users/charles/PycharmProjects/Games_Research/append_market_share/final(12_months).csv')