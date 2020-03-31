import os
import pandas as pd


bi_weekly_file_path = '/Users/charles/PycharmProjects/Games_Research/data/original_monthly_data/'


bi_weekly_file_list = os.listdir(bi_weekly_file_path)
bi_weekly_file_list.sort()
print(bi_weekly_file_list)
game_name_set=set()

for i in range(len(bi_weekly_file_list)):
    game_name_list={}
    #print(i)
    if i==0:
        game_name_list=pd.read_excel(bi_weekly_file_path+bi_weekly_file_list[i])['Game'].tolist()
        game_name_set=set(game_name_list)
    else:
        game_name_list=pd.read_excel(bi_weekly_file_path+bi_weekly_file_list[i])['Game'].tolist()
        current_game_set=set(game_name_list)
        game_name_set=game_name_set & current_game_set

    print(len(game_name_set))


game_name_set_df=pd.DataFrame(list(game_name_set),columns=['Game'])
print(game_name_set_df)
game_name_set_df.to_csv('/Users/charles/PycharmProjects/Games_Research/append_market_share/remain_games_name.csv')


