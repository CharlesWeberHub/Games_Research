from bs4 import BeautifulSoup as bs
import bs4
import pandas as pd
import os

name_score_df = pd.DataFrame(
    columns=['ID', 'Game', 'Owners before', 'Owners after', 'Sales', 'Increase', 'Price', 'Max discount',
             'Userscore (Metascore)'])
html_file = open(
    '/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/DATA/Calendar monthly(Source)/view-source_https___steamspy.com_sale.php_tagid=0&from=2020-03-01&to=2020-03-31&submit=.html',
    'r', encoding='utf-8')
html_handle = html_file.read()
soup = bs4.BeautifulSoup(html_handle, 'lxml')
all_tr = soup.find_all('tr')

count = 0
ind = 0

for tr_item in all_tr:
    ind += 1

    id_f = ''
    game_f = ''
    owners_before_f = ''
    owners_after_f = ''
    sales_f = ''
    increase_f = ''
    price_f = ''
    max_discount_f = ''
    u_m_score_f = ''

    try:
        tr_item.find('a')['href'].strip()
    except:
        continue

    href = tr_item.find('a')['href'].strip()

    if len(href) <= 25:
        continue

    if href[21:24] != 'app':
        continue

    count += 1
    id_f = href[25:]

    td_all_pre = tr_item.find_all('td')
    td_all_lat = all_tr[ind].find_all('td')[1]

    is_common_len = True
    no_mid_jump = True

    for i, child in enumerate(td_all_pre[1]):
        if child == ' ' and i == 0:
            is_common_len = False

        if child == ' ' and i == 3:
            no_mid_jump = False

    is_common_lat_len = True

    for i, child in enumerate(td_all_lat):
        if child == ' ' and i == 0:
            is_common_lat_len = False



    if is_common_len:
        for i, child in enumerate(td_all_pre[1]):
            if i == 3:
                game_f = child.string.strip()

            if i == 7:
                owners_before_f = child.string

            if i == 10:
                owners_after_f = child.string

            if i == 13:
                sales_f = child.string

            if i == 16:
                increase_f = child.string

            if i == 19:
                price_f = child.string
    else:
        for i, child in enumerate(td_all_pre[1]):
            if i == 3 + 1:
                game_f = child.string.strip()

            if i == 7 + 1:
                owners_before_f = child.string

            if i == 10 + 1:
                owners_after_f = child.string

            if i == 13 + 1:
                sales_f = child.string

            if i == 16 + 1:
                increase_f = child.string

            if i == 19 + 1:
                price_f = child.string

    if is_common_lat_len:
        for i, child in enumerate(td_all_lat):
            if i == 1:
                max_discount_f = child.string

            if i == 4:
                u_m_score_f = child.string
    else:
        for i, child in enumerate(td_all_lat):
            if i == 1 + 1:
                max_discount_f = child.string

            if i == 4 + 1:
                u_m_score_f = child.string

    name_score_df = name_score_df.append(
        [{'ID': id_f, 'Game': game_f, 'Owners before': owners_before_f, 'Owners after': owners_after_f,
          'Sales': sales_f, 'Increase': increase_f, 'Price': price_f, 'Max discount': max_discount_f,
          'Userscore (Metascore)': u_m_score_f}], ignore_index=True)


def convert_currency(var):
    """
    convert the string number to a float

    """
    new_value = var.replace(",", "").replace("$", "")
    return float(new_value)


# try:
#      name_score_df["Owners before"] = name_score_df["Owners before"].apply(convert_currency)
#      name_score_df["Owners after"] = name_score_df["Owners after"].apply(convert_currency)
#      name_score_df["Sales"] = name_score_df["Sales"].apply(convert_currency)
#      name_score_df["Price"] = name_score_df["Price"].apply(convert_currency)
#
# except:
#      print(id_f)


name_score_df.to_csv('ttttt.csv')
print(count)

# test_exc_df = pd.read_excel('/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/sss.xls')
# test_csv_df = pd.read_csv('/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/sss.csv')
#
# print(test_exc_df.info())
# print(test_csv_df.info())
#
#
# # test_exc_df["Sales"] = test_exc_df["Sales"].astype("int")
# # test_csv_df["Sales"] = test_csv_df["Sales"].astype("int")
#
# def convert_currency(var):
#     """
#     convert the string number to a float
#     _ 去除$
#     - 去除逗号，
#     - 转化为浮点数类型
#     """
#     new_value = var.replace(",", "").replace("$", "")
#     return float(new_value)
#
#
# test_exc_df["Sales"]=test_exc_df["Sales"].apply(convert_currency)
# test_csv_df["Sales"]=test_csv_df["Sales"].apply(convert_currency)
#
# print(test_exc_df.info())
# print(test_csv_df.info())
#
# print(test_exc_df.head())
# print(test_csv_df.head())
#
# test_exc_df.to_excel('x1.xls')
# test_csv_df.to_csv('x2.csv')

# html = """
#         <div class="c">
#             <a href="/u/">
#                 user
#             </a>
#             [所需内容]<h2>title</h2>
#             <span class="cc">
#                 bbb
#             </span>
#             <span class="ct">
#                 ccc
#             </span>
#         </div>
# """
#
# soup = bs(html, 'html.parser')
# div = soup.find('div', class_='c')
# all_contents = div.contents
#
#
# IS_FIRST_a = True
# IS_FIRST_span = True
# index_a = 0
# index_span = 0
#
# for i, child in enumerate(all_contents):
#     print(i, '----', child)
#     if child.name == 'a' and IS_FIRST_a:
#         index_a = i
#         IS_FIRST_a = False
#     if child.name == 'span' and IS_FIRST_span:
#         index_span = i
#         IS_FIRST_span = False
#
# print(index_a, index_span)
# content = all_contents[index_a + 1:index_span]
# print(content)
# want_content = []
# for text in content:
#     if type(text) is bs4.element.Tag:
#         want_content.append(text)
#     elif text.strip() != '':
#         want_content.append(text.strip())
#
# print(want_content)
