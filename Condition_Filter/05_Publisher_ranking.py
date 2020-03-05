import pandas as pd

game_features_df = pd.read_csv('/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(major_company).csv')
score_list = pd.read_csv('/Users/charles/PycharmProjects/Games_Research/Filter_HTML/score_list.csv')

score_list_name=score_list['Company_Name'].str.lower().tolist()

print(game_features_df.shape)

reputation_df = pd.DataFrame(columns=['Reputation'])

for index,row in game_features_df.iterrows():
    print(index)
    publisher=row['Publisher']
    if pd.isna(publisher):
        reputation_df = reputation_df.append([{'Reputation': ''}], ignore_index=True)
        continue

    is_found=0
    for list_item in score_list_name:
        if publisher in list_item:
            is_found=1
            reputation_df = reputation_df.append([{'Reputation': score_list_name.index(list_item)+1}], ignore_index=True)
            break
    if is_found==0:
        reputation_df = reputation_df.append([{'Reputation': ''}], ignore_index=True)

game_features_df['Reputation']=reputation_df[['Reputation']]
game_features_df.to_csv(
    '/Users/charles/PycharmProjects/Games_Research/Condition_Filter/games-features(reputation).csv')

#reputation_df.to_csv('/Users/charles/PycharmProjects/Games_Research/Condition_Filter/reputation_df.csv')

