import pandas as pd
from datetime import datetime

game_features_file_path = '/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(ex_owner_0).csv'
#game_features_file_path = '/Users/charles/PycharmProjects/Games_Research/Condition_Filter/test_data.csv'
game_features_df = pd.read_csv(game_features_file_path)

game_features_df=game_features_df[game_features_df['ReleaseDate']!=' ']

start_day = datetime(2020, 3, 3)
game_features_df['days'] = start_day - pd.to_datetime(game_features_df['ReleaseDate'])
game_features_df.to_csv('/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(days).csv')

game_features_df = pd.read_csv('/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(days).csv')

game_features_df['age'] = game_features_df['days'].str.split('days', 1).str[0]
game_features_df['age'] = game_features_df['age'].str.strip()

print(game_features_df.info())

game_features_df['one'] = 30
game_features_df['age'] = game_features_df['age'].astype('int').div(game_features_df['one'])
game_features_df['age'] = game_features_df['age'].astype('int') + 1

game_features_df=game_features_df[game_features_df['age']>=3]

print(game_features_df.info())

game_features_df.to_csv('/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(age).csv')
