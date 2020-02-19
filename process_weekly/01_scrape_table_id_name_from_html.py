from bs4 import BeautifulSoup
import pandas as pd

html_file_path = '/data/bi_weekly_data/html_files/2018-12-18 to 2019-03-11.html'
html_file = open(html_file_path, 'r', encoding='utf-8')
html_handle = html_file.read()

id_name_df = pd.DataFrame(columns=['ID', 'Name'])

soup = BeautifulSoup(html_handle, 'lxml')
all_tr = soup.find_all('tr')

for tr_item in all_tr:
    id_name_df = id_name_df.append([{'ID':tr_item.find('a')['href'][5:].strip(),'Name':tr_item.find('a').text.strip()}], ignore_index=True)
    # print(tr_item.find('a')['href'][5:])
    # print(tr_item.find('a').text)

print(id_name_df)
id_name_df.to_csv('/Users/charles/PycharmProjects/Games_Research/data/steam_spy_id_name_list_from_html_table/all_id_name 2018-12-18 to 2019-03-11.csv')

# count = 0
# result = pd.DataFrame({},index=[0])
# result['author'] = ''
# result['title'] = ''
# result['source'] = ''
# new = result
# for item in soup.find_all('tr'):
#     if 'AU ' in item.get_text():
#         author = item.get_text()
#         new['author'] = author
#     elif 'TI ' in item.get_text():
#         title = item.get_text()
#         new['title'] = title
#     elif 'SO ' in item.get_text():
#         source = item.get_text()
#         new['source'] = source
#         count += 1
#         result = result.append(new,ignore_index=True)
# print(count)