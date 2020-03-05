import pandas as pd
from datetime import datetime

game_features_file_path = '/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(major_company).csv'
# game_features_file_path = '/Users/charles/PycharmProjects/Games_Research/Condition_Filter/test_data.csv'
game_features_df = pd.read_csv(game_features_file_path)
game_features_df = game_features_df.loc[(game_features_df["ReleaseDate"] != 'Coming Soon') & (
        game_features_df["ReleaseDate"] != 'Coming to home video Q1 2020')]


print(game_features_df.info())


def type_filter(a):
    try:
        pd.to_datetime(a.strip())
        return a.strip()
    except:
        return ''


game_features_df['Value'] = game_features_df.apply(lambda row: type_filter(row['ReleaseDate']), axis=1)

game_features_df = game_features_df[game_features_df['Value'] != '']
print(game_features_df.info())

start_day = datetime(2020, 3, 3)
game_features_df['days'] = start_day - pd.to_datetime(game_features_df['ReleaseDate'])
game_features_df.to_csv('/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(days).csv')

game_features_df = pd.read_csv(
    '/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(days).csv')

game_features_df['age'] = game_features_df['days'].str.split('days', 1).str[0]
game_features_df['age'] = game_features_df['age'].str.strip()

print(game_features_df.info())

game_features_df['one'] = 30
game_features_df['age'] = game_features_df['age'].astype('int').div(game_features_df['one'])
game_features_df['age'] = game_features_df['age'].astype('int') + 1

game_features_df = game_features_df.drop(["days"], axis=1)
game_features_df = game_features_df.drop(["one"], axis=1)
game_features_df.to_csv('/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(age>3).csv')

game_features_df = game_features_df[game_features_df['age'] >= 3]

game_features_df=game_features_df.drop(["Unnamed: 0.1.1"],axis=1)
game_features_df=game_features_df.drop(["Unnamed: 0.1"],axis=1)
game_features_df=game_features_df.drop(["Unnamed: 0"],axis=1)

print(game_features_df.info())
game_features_df.to_csv('/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(age>3).csv')
