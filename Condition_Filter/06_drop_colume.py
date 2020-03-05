import pandas as pd

game_features_df = pd.read_csv('/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(ex_owner_0).csv')

print(game_features_df.info())
game_features_df=game_features_df.drop(["Unnamed: 0.1.1.1.1.1"],axis=1)
game_features_df=game_features_df.drop(["Unnamed: 0.1.1.1.1"],axis=1)
game_features_df=game_features_df.drop(["Unnamed: 0.1.1.1"],axis=1)
game_features_df=game_features_df.drop(["Unnamed: 0.1.1"],axis=1)
game_features_df=game_features_df.drop(["Unnamed: 0.1"],axis=1)
game_features_df=game_features_df.drop(["Unnamed: 0"],axis=1)
game_features_df=game_features_df.drop(["Value"],axis=1)
print(game_features_df.info())
game_features_df.to_csv('/Users/charles/PycharmProjects/Games_Research/Condition_Filter/results/games-features(final).csv')