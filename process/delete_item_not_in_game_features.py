# Delete the id no exits in the games-features.csv but exits in Match id_name.csv
import os
import pandas as pd

file_path = '/Users/charles/Desktop/Compress/Downloads'

# The file that we need to merge
file_list = os.listdir(file_path)
file_list.sort()

# The time that is for us to analysis
time_period_list = []

id_name = pd.read_csv('Match id_name.csv')[['ID', 'Name']]
res_id_name = pd.read_csv('games-features.csv')[['ResponseID', 'ResponseName']]

del_count=0

print('delete_before: ' +str(id_name.shape[0]))

for index, row in id_name.iterrows():
    # find the id exits in the games-features.csv
    result_match = res_id_name.loc[res_id_name['ResponseID'] == row['ID']]
    if result_match.shape[0] < 1:
        # find the id no exits in the games-features.csv but exits in Match id_name.csv
        current_index = id_name.loc[id_name['ID'] == row['ID']].index.tolist()[0]
        # print(current_index)
        # delete the items in Match id_name.csv
        id_name=id_name.drop(index=current_index)
        del_count+=1

print('delete_after: ' +str(id_name.shape[0]))

print(del_count)

id_name.to_csv('Match id_name.csv')