import pandas as pd
import os

monthly_data_path = '/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/OUTPUT_DATA/Calendar_monthly_csv/'

monthly_data_file_list = os.listdir(monthly_data_path)
monthly_data_file_list.sort()

game_id_set=set()

max_period=''
max_count=0

for i in range(len(monthly_data_file_list)):

    if 6+i>len(monthly_data_file_list):
        break

    period = monthly_data_file_list[0+i][0:13]+monthly_data_file_list[5+i][13:24]
    print(period)

    game_id_list = {}
    for i, file in enumerate(monthly_data_file_list[0+i:6+i]):
        if i==0:
            game_id_list=pd.read_csv(monthly_data_path+file)['ID'].tolist()
            game_id_set=set(game_id_list)
        else:
            game_id_list=pd.read_csv(monthly_data_path+file)['ID'].tolist()
            current_game_set=set(game_id_list)
            game_id_set=game_id_set & current_game_set

    set_len=len(game_id_set)
    if set_len>max_count:
        max_period=period
        max_count=set_len

    print(set_len)

print('max_period: '+ str(max_period))
print('max_count: '+ str(max_count))