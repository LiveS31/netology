import requests
import json
from fake_headers import Headers
from bs4 import BeautifulSoup

hh_url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

def get_handres():
    return Headers(browser='firefox', os='win').generate()

def main_pg():
    main_padge = requests.get(hh_url, headers=get_handres()).text
    # print(main_padge)
    bs = BeautifulSoup(main_padge, features='lxml')
    list_hh = bs.find_all('span', class_="bloko-header-section-3")
    a = bs.find_all(class_="serp-item__title")
    print(list_hh)
    print((a))
    for b in a:
        print(b['href'])
main_pg()