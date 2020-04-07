import pandas as pd
import os
import copy

game_features_path = '/Users/charles/PycharmProjects/Games_Research/data/game_feature/games-features(40604 rows).csv'

game_features_df = pd.read_csv(game_features_path)

current_index = game_features_df[game_features_df['QueryID'] == 219740].index[0]
game_features_df.loc[current_index, 'ReleaseDate'] = 'Apr 23 2013'
game_features_df.to_csv('/Users/charles/PycharmProjects/Games_Research/data/game_feature/games-features(40604 rows & add release date ).csv')