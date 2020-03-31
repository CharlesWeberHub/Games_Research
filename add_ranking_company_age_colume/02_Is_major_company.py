import pandas as pd

game_features_df = pd.read_csv('/Users/charles/PycharmProjects/Games_Research/add_ranking_company_age_colume/games-features(reputation).csv')
major_company_file_path = '/Users/charles/PycharmProjects/Games_Research/data/monthly_data/major_company/'
major_company = pd.read_csv(major_company_file_path + 'MajorCompany.csv')
company_list = pd.concat(major_company.iloc[:, i] for i in range(1, major_company.shape[1]))
company_list.index = pd.np.arange(len(company_list))
company_list = company_list.dropna().unique().tolist()
# print(type(company_list))
# print(len(company_list))
company_list = [item.lower() for item in company_list]
print(company_list)


def string_finder(columns, words):
    if any(word in field for field in columns for word in words):
        return True
    return False


game_features_df[['Publisher']] = game_features_df['Publisher'].str.lower()

game_features_df['isMajorCompany'] = game_features_df[['Publisher']].astype(str).apply(string_finder,
                                                                                       words=company_list, axis=1)
print(game_features_df.info())

game_features_df.to_csv(
    '/Users/charles/PycharmProjects/Games_Research/add_ranking_company_age_colume/games-features(major_company).csv')
