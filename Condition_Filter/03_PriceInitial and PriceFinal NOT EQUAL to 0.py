import pandas as pd

game_features_file_path = '/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(major_company).csv'
game_features_df = pd.read_csv(game_features_file_path)
print(game_features_df.info())
game_features_df = game_features_df.loc[(game_features_df["PriceInitial"] != 0) & (game_features_df["PriceFinal"] != 0)]
print(game_features_df.info())
game_features_df.to_csv('/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(ex_price_0).csv')
