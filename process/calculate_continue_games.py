import os
import pandas as pd

weekly_file_path = '/Users/charles/Desktop/Raw_data/Downloads/'


weekly_file_list = os.listdir(weekly_file_path)
weekly_file_list.sort()

#print(len(weekly_file_list))

game_name_set=set()

for i in range(len(weekly_file_list)):
    game_name_list={}
    #print(i)
    if i==0:
        game_name_list=pd.read_excel(weekly_file_path+weekly_file_list[i])['Game'].tolist()
        game_name_set=set(game_name_list)
    else:
        game_name_list=pd.read_excel(weekly_file_path+weekly_file_list[i])['Game'].tolist()
        current_game_set=set(game_name_list)
        game_name_set=game_name_set & current_game_set

    print(len(game_name_set))
