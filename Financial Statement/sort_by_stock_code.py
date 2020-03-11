import pandas as pd

df_stock_list = pd.read_csv('/Users/charles/PycharmProjects/Games_Research/Financial Statement/game_stock_code(edited).csv')
df_stock_list = df_stock_list.sort_values(by='code', ascending=True)
df_stock_list = df_stock_list.reset_index()
df_stock_list[['code','name','c_name']].to_csv('/Users/charles/PycharmProjects/Games_Research/Financial Statement/game_stock_code(sorted).csv')
