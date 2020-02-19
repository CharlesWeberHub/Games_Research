import os
import pandas as pd

# weekly_file_path = '/Users/charles/Desktop/Raw_data/Downloads/'
#
#
# weekly_file_list = os.listdir(weekly_file_path)
# weekly_file_list.sort()


# game_name_set=set()
#
# for i in range(len(weekly_file_list)):
#     game_name_list={}
#     #print(i)
#     if i==0:
#         game_name_list=pd.read_excel(weekly_file_path+weekly_file_list[i])['Game'].tolist()
#         game_name_set=set(game_name_list)
#     else:
#         game_name_list=pd.read_excel(weekly_file_path+weekly_file_list[i])['Game'].tolist()
#         current_game_set=set(game_name_list)
#         game_name_set=game_name_set & current_game_set
#
#     print(len(game_name_set))
#
bi_weekly_file_path = '/data/bi_weekly_data/biweekly/'


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
game_name_set_df.to_csv('/Users/charles/PycharmProjects/Games_Research/data/remain_games/remain_games_name_2018-12-18 to 2019-03-11.csv')



# monthly_file_path = '/Users/charles/Desktop/Raw_data/recolloect/Monthly/'
#
# monthly_file_list = os.listdir(monthly_file_path)
# monthly_file_list.sort()
# print(monthly_file_list)
# game_name_set = set()
#
# for i in range(len(monthly_file_list)):
#     game_name_list = {}
#     # print(i)
#     if i == 0:
#         game_name_list = pd.read_csv(monthly_file_path + monthly_file_list[i], engine='python')['Game'].tolist()
#         game_name_set = set(game_name_list)
#     else:
#         game_name_list = pd.read_csv(monthly_file_path + monthly_file_list[i], engine='python')['Game'].tolist()
#         current_game_set = set(game_name_list)
#         game_name_set = game_name_set & current_game_set
#
#     print(len(game_name_set))
#
# print(game_name_set)