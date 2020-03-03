import pandas as pd

game_features_file_path = '/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(ex_price_0).csv'
game_features_df = pd.read_csv(game_features_file_path)
game_features_df = game_features_df.loc[(game_features_df["SteamSpyOwners"] != 0) ]
print(game_features_df.info())
