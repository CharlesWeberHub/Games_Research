import pandas as pd
import os
from bs4 import BeautifulSoup

monthly_data_path = '/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/DATA/Calendar monthly(Source)/'
quarterly_data_path = '/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/DATA/Calendar quarterly(Source)/'

monthly_data_output_csv_path = '/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/OUTPUT_DATA/Calendar_monthly_csv/'
monthly_data_output_excel_path = '/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/OUTPUT_DATA/Calendar_monthly_excel/'

quarterly_data_output_csv_path = '/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/OUTPUT_DATA/Calendar_quarterly_csv/'
quarterly_data_output_excel_path = '/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/OUTPUT_DATA/Calendar_quarterly_excel/'

monthly_data_file_list = os.listdir(monthly_data_path)
monthly_data_file_list.sort()
quarterly_data_file_list = os.listdir(quarterly_data_path)
quarterly_data_file_list.sort()

for i, file in enumerate(monthly_data_file_list):
    print(i, file)
    output_filename_csv = file[55:65] + ' to ' + file[69:79] + ' (monthly_data).csv'
    output_filename_excel = file[55:65] + ' to ' + file[69:79] + ' (monthly_data).xls'

    name_score_df = pd.DataFrame(
        columns=['ID', 'Game', 'Owners before', 'Owners after', 'Sales', 'Increase', 'Price', 'Max discount',
                 'Userscore (Metascore)'])
    html_file = open(monthly_data_path + file, 'r', encoding='utf-8')
    html_handle = html_file.read()
    soup = BeautifulSoup(html_handle, 'lxml')
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

        # special_1
        no_special_case=True

        for i, child in enumerate(td_all_pre[1]):
            if child == ' ' and i == 0:
                is_common_len = False

            if child == ' ' and i == 3:
                no_mid_jump = False

            if i>22:
                no_special_case=False


        is_common_lat_len = True

        for i, child in enumerate(td_all_lat):
            if child == ' ' and i == 0:
                is_common_lat_len = False

        if not no_mid_jump:
            print(id_f)
            for i, child in enumerate(td_all_pre[1]):
                print(i, '----', child)

                if no_special_case:
                    if i == 0:
                        all_in_span = child.find_all('span')
                        if len(all_in_span)==1:
                            game_f=''
                        if len(all_in_span)>1:
                            game_f = all_in_span[1].get_text()

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
                    if i == 0:
                        all_in_span = child.find_all('span')
                        if len(all_in_span) == 1:
                            game_f = ''
                        if len(all_in_span) > 1:
                            game_f = all_in_span[1].get_text()

                    if i == 10:
                        owners_before_f = child.string

                    if i == 13:
                        owners_after_f = child.string

                    if i == 16:
                        sales_f = child.string

                    if i == 19:
                        increase_f = child.string

                    if i == 22:
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

            continue

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

    print('count: ' + str(count))

    def convert_currency(var):
        """
        convert the string number to a float

        """
        new_value = var.replace(",", "").replace("$", "")
        return float(new_value)

    #
    # try:
    #      name_score_df["Owners before"] = name_score_df["Owners before"].apply(convert_currency)
    #      name_score_df["Owners after"] = name_score_df["Owners after"].apply(convert_currency)
    #      name_score_df["Sales"] = name_score_df["Sales"].apply(convert_currency)
    #      name_score_df["Price"] = name_score_df["Price"].apply(convert_currency)
    #
    # except:
    #      print('error')
    #      continue

    name_score_df["Owners before"] = name_score_df["Owners before"].apply(convert_currency)
    name_score_df["Owners after"] = name_score_df["Owners after"].apply(convert_currency)
    name_score_df["Sales"] = name_score_df["Sales"].apply(convert_currency)
    name_score_df["Price"] = name_score_df["Price"].apply(convert_currency)

    name_score_df.to_csv(monthly_data_output_csv_path + output_filename_csv)
    name_score_df.to_csv(monthly_data_output_excel_path + output_filename_excel)
    print(name_score_df.info())

