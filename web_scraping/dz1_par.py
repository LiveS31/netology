import requests
import json
from fake_headers import Headers
from bs4 import BeautifulSoup

hh_url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

def get_handres():
    return Headers(browser='firefox', os='win').generate()

main_padge = requests.get(hh_url, headers=get_handres()).text
#print(main_padge)
bs = BeautifulSoup(main_padge, features='lxml')
list_hh = bs.find_all(class_="serp-item__title")

a_temp = []
a_temp1 = []
for txt in list_hh:
    a_temp.append({
        'vaca': txt.text,
        'link': txt['href']
                })

print(a_temp)
a_a = []
list_hh1 = bs.find_all('span',class_="bloko-header-section-3")
for zp in list_hh1:
    zzp = zp.text.replace("\u202f", " ")
    a_a.append({
        'zp': zzp}) # обход неразрывноного пробела в юникоде
print(a_a)


#     a_a.append(zp.text)
# print (a_a)

# with open('data_file.json', 'w', encoding='utf-8') as data:
#     json.dump(zp.text, data, indent=2, ensure_ascii=False)






