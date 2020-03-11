import tushare as ts

concept_classified = ts.get_concept_classified()
concept_classified.to_csv('/Users/charles/PycharmProjects/Games_Research/Financial Statement/concept_classified.csv')

print(type(concept_classified))