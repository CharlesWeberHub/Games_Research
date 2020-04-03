import os
import pandas as pd

writer = pd.ExcelWriter('/Users/charles/PycharmProjects/Games_Research/append_market_share/result.xlsx',engine='openpyxl')

_12_months_uncomplete_observation_path='/Users/charles/PycharmProjects/Games_Research/append_market_share/gamedata(owner_change_without_complete_observation).xls'
_6_months_path = '/Users/charles/PycharmProjects/Games_Research/append_market_share/final(6_months).csv'
_12_months_path = '/Users/charles/PycharmProjects/Games_Research/append_market_share/final(12_months).csv'

sheet_names = ["12_months_uncomplete_observation","6_months_complete_observation","12_months_complete_observation"]

_12_months_uncomplete_observation_df=pd.read_excel(_12_months_uncomplete_observation_path)
_6_months_df=pd.read_csv(_6_months_path)
_12_months_df=pd.read_csv(_12_months_path)

_12_months_uncomplete_observation_df.to_excel(excel_writer=writer, sheet_name=sheet_names[0], encoding="utf-8", index=False)
_6_months_df.to_excel(excel_writer=writer, sheet_name=sheet_names[1], encoding="utf-8", index=False)
_12_months_df.to_excel(excel_writer=writer, sheet_name=sheet_names[2], encoding="utf-8", index=False)
writer.save()
writer.close()