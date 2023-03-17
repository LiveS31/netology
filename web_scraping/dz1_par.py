mix_sort = {'adres': ['Москва, Кутузовская, Кутузовская, Кутузовский проспект, 32к1',
           'Санкт-Петербург, Тарасова улица, 12/18',
           'Москва',
           'Москва',
           'Санкт-Петербург, Выборгская, Выборгская набережная, 49Б',
           'Москва, Кузнецкий мост, Лубянка, Трубная, Малый Кисельный '
           'переулок, 1/9',
           'Брест, Пионерская улица, 52',
           'Москва, Западный административный округ, Можайский район, '
           'Инновационный центр Сколково, улица Нобеля, 5',
           'Москва'],
 'jobs': ['Сбер. IT',
          'ООО Единая Информационная Система ЖКХ',
          'ООО Фабрика Решений',
          'WorkinGeeks',
          'ITRestoran(ООО Титул)',
          'АНО Инфокультура',
          'ООО Арктический 12',
          'JetLend',
          '4CV Recruitment Services'],
 'link-on': ['https://spb.hh.ru/vacancy/75888105?from=vacancy_search_list&query=python',
             'https://spb.hh.ru/vacancy/77871173?from=vacancy_search_list&query=python',
             'https://spb.hh.ru/vacancy/70705466?from=vacancy_search_list&query=python',
             'https://spb.hh.ru/vacancy/77716464?from=vacancy_search_list&query=python',
             'https://spb.hh.ru/vacancy/78033814?from=vacancy_search_list&query=python',
             'https://spb.hh.ru/vacancy/77873430?from=vacancy_search_list&query=python',
             'https://spb.hh.ru/vacancy/77992483?from=vacancy_search_list&query=python',
             'https://spb.hh.ru/vacancy/78083627?from=vacancy_search_list&query=python',
             'https://spb.hh.ru/vacancy/77853688?from=vacancy_search_list&query=python'],
 'zap': ['з/п не указана',
         'от 90 000 до 150 000 руб. на руки',
         'от 60 000 до 220 000 руб. на руки',
         'от 180 000 руб. на руки',
         'до 150 000 руб. до вычета налогов',
         'от 150 000 до 180 000 руб. на руки',
         'от 2 500 до 4 500 USD до вычета налогов',
         'до 150 000 руб. на руки',
         'от 7 000 до 9 000 USD до вычета налогов']}
from pprint import pprint

import json
temp = []
for a in range (len(mix_sort['adres'])):
    if 'Москва' in mix_sort['adres'][a] or 'Санкт-Петербург' in mix_sort['adres'][a]:
        temp.append({
           'адрес': (mix_sort['adres'][a]),
            'работодатель': (mix_sort['jobs'][a]),
            'ссылка на вакансию': (mix_sort['link-on'][a]),
            'зарплата': (mix_sort['zap'][a])
        })
  #  else:
   #     continue
with open('data.json', 'w') as f:
    json.dump(temp, f, ensure_ascii=False, indent=4)

