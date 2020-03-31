import pandas as pd

final_file_path = '/Users/charles/PycharmProjects/Games_Research/append_market_share/final.csv'

final_df=pd.read_csv(final_file_path)

final_df=final_df.drop(["Unnamed: 0.1"],axis=1)
final_df=final_df.drop(["Unnamed: 0"],axis=1)

final_df.to_excel('/Users/charles/PycharmProjects/Games_Research/append_market_share/gamedata(owner_change).xls')

print(final_df.info())