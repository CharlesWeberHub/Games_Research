from bs4 import BeautifulSoup
import pandas as pd

html_file_path = '/Users/charles/PycharmProjects/Games_Research/Filter_HTML/score_list.html'
html_file = open(html_file_path, 'r', encoding='utf-8')
html_handle = html_file.read()

name_score_df = pd.DataFrame(columns=['Company_Name', 'Score'])

soup = BeautifulSoup(html_handle, 'lxml')
all_li = soup.find_all('li')

for li_item in all_li:
    print(li_item.find('a').text.strip())
    print(li_item.find('strong').text[15:].strip())

    name_score_df = name_score_df.append([{'Company_Name':li_item.find('a').text.strip(),'Score':li_item.find('strong').text[15:].strip()}], ignore_index=True)


print(name_score_df)
name_score_df.to_csv('/Users/charles/PycharmProjects/Games_Research/Filter_HTML/score_list.csv')

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