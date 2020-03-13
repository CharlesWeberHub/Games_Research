import pandas as pd

temp_file_path = '/Users/charles/PycharmProjects/Games_Research/append_market_share/temp_id_name.csv'
monthly_file_path = '/Users/charles/PycharmProjects/Games_Research/data/original_monthly_data/Steam sales from2019-08-12 to2019-09-08 - SteamSpy - All the data and stats about Steam games.xlsx'
result_game_path = '/Users/charles/PycharmProjects/Games_Research/append_market_share/gamedata.csv'

id_sales_df = pd.DataFrame(columns=['Sales'])

temp_file_df = pd.read_csv(temp_file_path)
month_data_df = pd.read_excel(monthly_file_path)
result_game_df = pd.read_csv(result_game_path)

result_game_df['Sales']=id_sales_df['Sales']

for index, row in temp_file_df.iterrows():
    #得到匹配中的那一行，包含销售数据
    name_match = month_data_df.loc[month_data_df['Game'] == row['Name']]

    current_index=result_game_df[result_game_df['QueryID'] == row['ID']].index[0]

    result_game_df.loc[current_index, 'Sales']=name_match['Sales'].iloc[0]



print(result_game_df.info())