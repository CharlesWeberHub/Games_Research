import os
import pandas as pd
from bs4 import BeautifulSoup

genre_file_path = '/Users/charles/PycharmProjects/Games_Research/IV_append/data_sourse/'
genre_excel_output_path='/Users/charles/PycharmProjects/Games_Research/IV_append/genre_excel/'
genre_file_list = os.listdir(genre_file_path)
genre_file_list.sort()

id_name_df = pd.DataFrame(columns=['ID', 'Game'])

for i in range(10, len(genre_file_list)):
    genre_name = genre_file_list[i][39:].split('.', 1)[0]
    print(genre_name)
    html_file = open(genre_file_path + genre_file_list[i], 'r', encoding='utf-8')
    html_handle = html_file.read()
    soup = BeautifulSoup(html_handle, 'lxml')
    all_tr = soup.find_all('tr')
    count = 0
    ind = 0

    for tr_item in all_tr:
        ind += 1
        id_f = ''
        game_f = ''

        try:
            tr_item.find('a')['href'].strip()
        except:
            continue

        href = tr_item.find('a')['href'].strip()

        if len(href) <= 25:
            continue

        if href[21:24] != 'app':
            continue

        id_f = href[25:]

        td_all_pre = tr_item.find_all('td')

        is_common_len = True

        for i, child in enumerate(td_all_pre[1]):
            if child == ' ' and i == 0:
                is_common_len = False

        if is_common_len:
            for i, child in enumerate(td_all_pre[1]):
                if i == 3:
                    game_f = child.string

        else:
            for i, child in enumerate(td_all_pre[1]):
                if i == 3+1:
                    game_f = child.string

        try:
            id_name_df = id_name_df.append(
                [{'ID': id_f, 'Game': game_f.strip()}], ignore_index=True)
        except:
            for i, child in enumerate(td_all_pre[1]):
                print(child)
            break
        count += 1

    print(count)
    print(genre_name)
    print(id_name_df.info())
    id_name_df.to_csv(genre_excel_output_path+genre_name+'.csv')
    break

