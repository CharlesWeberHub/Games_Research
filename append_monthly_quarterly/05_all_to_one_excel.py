import os
import pandas as pd
import xlsxwriter

writer = pd.ExcelWriter('/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/result.xls',engine='xlsxwriter')

_6_months_path = '/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/new_form(6_months_split_discount).csv'
_12_months_path = '/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/new_form(12_months_split_discount).csv'
_6_quarters_path = '/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/new_form(6_quarters_split_discount).csv'

sheet_names = ["6_months","12_months","6_quarters"]


_6_months_df=pd.read_csv(_6_months_path)
_12_months_df=pd.read_csv(_12_months_path)
_6_quarters_df=pd.read_csv(_6_quarters_path)

_6_months_df.to_excel(excel_writer=writer, sheet_name=sheet_names[0], encoding="utf-8", index=False)
_12_months_df.to_excel(excel_writer=writer, sheet_name=sheet_names[1], encoding="utf-8", index=False)
_6_quarters_df.to_excel(excel_writer=writer, sheet_name=sheet_names[2], encoding="utf-8", index=False)

writer.save()
writer.close()