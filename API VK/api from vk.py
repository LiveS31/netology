#API - сервис взаимодействия программ /опер систем/.....
# Аутофикация -доступ (процедура проверки пользователя)
# Авторизация - вход (предоставление определенному лицу прав на выполнение определенных действий)

# Один из протаколов авторизвции протокол OAuth

# scop - параметры достопа приложения в параметрах полученного токена

#Синтаксис запроси в vk
#https://api.vk.com/metod/(название метода)/PARAMS&access_token=TOKENv=V
#Данные можно получить данные/ начало wall.метод
#далее примеры запросов

import time # таймер модуля времени для ограничения кол-во запросов

token = 'vk1.a.bNuuXGlvNJmZVNVnuQs2DDbPwBkIRl6Gns60G8Zdnv-Y_XrDeXzqpVKhYtHr_xduyP09A-'
import requests #для отправки запросов по api
from pprint import pprint #чтобы красиво выводить сложные, вложенные объекты
#import pandas as pd
#pd.DataFrame(vk_client.search_groups_exit('python'))# красивая и удобная таблица

url = 'https://api.vk.com/method/users.get'
params = {
    'user_ids': '1', # id - пользователя по которому получить информацию
    'access_token': token, # передаем токен (токен т версия api является обязательной
    'v': '5.131',# версия api (является обязательной для вконтакте
    'fields': 'education,sex'# подобным образом добавлям данные которые мы хотим получить.
}
res = requests.get(url,params=params) # делаем запрос по адресу с параметрами
pprint(res.json())
# потренироваться получать токен во вконтакте
#Функция для поиска групп соц сети вконтакте
def search_groups (q, sorting=0):
    #Параметры sotr
# 0 - сортировать по умолчанию (аналог поиска в полной версии сайта)
# 6 - сортироовать по колличеству пользователей
    params ={
    'q':q,
    'access_token': token,
    'v':'5.131',
    'sort': sorting,
    'coun':100
    }

    req = requests.get('https://api.vk.com/method/groups.search', params).json()
    pprint(res)
    req = req['response']['items'], req
    return req
# получаем три словаря. 1. response, 2. items - и по тем же ключам все достаем (count - общее число групп,
# items - список из конкретных групп
target_groups=search_groups('kia').get
pprint(target_groups)
# Преобразуем список всех id в строку (в таком виде принимает данные параметр fields)
# добавляем информацию о группах (берем их id). Для этого:
#         target_group_ids = ','.join([str(group['id']) for groups in target_groups])
#         pprint (target_group_ids)
# #узнаем более детальную информацию о группах
#     params = {
#         'access_token': token,
#         'v': '5.131',
#         'groups_ids': target_group_ids,
#         'fields': 'members_count.activity.description'
#     }

# req = requests.get('https://api.vk.com/method/groups.getById', params)
# pprint(req.json()['response'])
#как это сделать в классах
#токен и версия могут быть разные
#базовый url - будет вседа один
#class VkUser:
    # url = 'https://api.vk.com/method/'
    # def __init__(self, token, version):
    #     self.params = {
    #         'access_token' : token,
    #         'v': version
    #     }
    # def search_groups(self, q, soring=0):
    #      #Пвраметры sort
    #     # 0 - сортировка по умолчанию (аналогично результатам поиска не полной версии сайта)
    #     # 6 - сортировка по количеству пользователей
    #     group_search_url = self.url+'groups.search'
    #     group_search_params = {'q': q,
    #                            'sort':sorting,
    #                            'count': 300
    #                            }
    #
    #     req = requests.get(group_search_url, params={**self.params, **groups_search_params}).json()# объединение словарей в один (в params)
    #     return req ['response']['item']
    # def search_groups_exit(self, q, sorting=0):
    #     groups_search_ext_url = self.url+ 'groups.getById'
    #     target_groups = self.search_groups(q, sorting)
    #     target_groups_ids = '.'.join([str(group['id']) for group in target_groups])
    #     group_info_params= {
    #         'group_id': target_groups_ids,
    #         'fieds': 'members_count.activity, description'
    #     }
    #     reg = requests.get(groups_search_ext_url, params={**self.params, **groups_info_params}).json()# объединение словарей в один (в params)
    #     return req ['resource']
# {**self.params, **groups_info_params} - ** распаковывают словари и так как стоят фигурные скобки - словари объединяются в один

# получаем подписчиков
#     def get_follwers(self, user_id = None):
#         followers_url = self.url +'users.getFollwers'
#         followers_params = {
#             'count': 2,
#             'user_id': user_id
#         }
#         res = requests.get(followers_url, params={**self.params, **followers_params}).json()
#         return res ['resource']
#vk_client.get_followers('1')#получение подписчиков пользователя 1
#получаем данные циклом
    # def get_news(self, query):
    #     groups_url = self.url+'newsfeed.search'
    #     groups_params = {
    #         'q' = query,
    #     'count': 200
       # }
#newsfeed_df = pd.DataFrame()
#     while True:
#         result = requests.get(groups_url, params=[**self.params, **groups_params])
#         time.sleep(0.33) #- задержка запроса
#         newsfeed_df = pd.concat([newsfeed_df,pd.DataFrame(result.json()['response']['item'])])
#         if 'next_from' in result.json()['response']:
#             groups_params['start_from'] = result.json()['response']['next_from']
#         else:
#             break
#     return newsfeed_df
# #vk_client = VkUser(token,'5.1
#newsfeed_df = pd.DataFrame()
     # while True:
     #     result = requests.get(groups_url, params={**self.params, **groups_params})
     #     time.sleep(0.33) #- задержка запроса
     #     newsfeed_df = pd.concat([newsfeed_df,pd.DataFrame(result.json()['response']['item'])])
     #     if 'next_from' in result.json()['response']:
     #         groups_params['start_from'] = result.json()['response']['next_from']
     #     else:
     #         break
     # return newsfeed_df
# vk_client = VkUser(token,'5.131')
# vk_client.get_news('короновирус')
#vk_client.get_news('короновирус')