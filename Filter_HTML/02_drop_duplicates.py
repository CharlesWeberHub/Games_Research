import pandas as pd

file_path = '/Users/charles/PycharmProjects/Games_Research/Filter_HTML/score_list.csv'

name_score_df = pd.read_csv(file_path)

name_score_df = name_score_df.drop_duplicates(subset=['Company_Name'], keep='first')

name_score_df[['Company_Name', 'Score']].to_csv('/Users/charles/PycharmProjects/Games_Research/Filter_HTML/score_list_drop_duplicates.csv')