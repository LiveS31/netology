from settings import TOKEN_VK, KEY_GROUP
from pprint import pprint
import json
import datetime
import vk_api
import configparser

config = configparser.ConfigParser()
config.read('pass.ini')

def get_info_users(id_user):
    id_user = id_user
    vk = vk_api.VkApi(token= config['vk']['KEY_GROUP'])
    response = vk.method('users.get', {'user_ids': id_user, 'fields': 'city, sex, bdate'})
    user_info = [response[0]['id'], response[0]['first_name'], response[0]['last_name'],
                 response[0]['sex'], response[0]['city']['title'], f'https://vk.com/id{response[0]["id"]}']
    return user_info


def search_users(sex, age_from, age_to, city):
    all_persons = []
    link_profile = 'https://vk.com/id'
    vk = vk_api.VkApi(token= config['vk']['TOKEN_VK'])
    response = vk.method('users.search',
                         {'sort': 1,
                          'sex': sex,
                          'status': 1,
                          'age_from': age_from,
                          'age_to': age_to,
                          'has_photo': 1,
                          'count': 25,
                          'online': 1,
                          'hometown': city
                          })
    for element in response['items']:
        person = [
            element['first_name'],
            element['last_name'],
            link_profile + str(element['id']),
            element['id']
        ]
        all_persons.append(person)
    return all_persons


def get_photo(owner_id):
    try:
        vk = vk_api.VkApi(token= config['vk']['TOKEN_VK'])
        response = vk.method('photos.get',
                             {'owner_id': owner_id,
                              'album_id': 'profile',
                              'count': 10,
                              'extended': 1,
                              'photo_sizes': 1})
        users_photos = []
        for i in range(len(response['items'])):
            users_photos.append(
                [response['items'][i]['likes']['count'],
                 response['items'][i]['sizes'][-1]['url']])
        return users_photos
    except(vk_api.exceptions.ApiError, TypeError):
        pass


def sort_photo(photo_list):
    try:
        sort_list = sorted(photo_list, key=lambda x: int(x[0]), reverse=True)
        return sort_list[:3]
    except(vk_api.exceptions.ApiError, TypeError):
        return ['нет фото']


def create_json(lst):
    today = datetime.date.today()
    today_str = f'{today.day}.{today.month}.{today.year}'
    result = {}
    result_list = []
    for num, info in enumerate(lst):
        result['data'] = today_str
        result['first_name'] = info[0]
        result['second_name'] = info[1]
        result['link'] = info[2]
        result['id'] = info[3]
        result_list.append(result.copy())
    with open("result.json", "a", encoding='UTF-8') as write_file:
        json.dump(result_list, write_file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    pprint(get_info_users(1))
    pprint(search_users(2, 18, 40, 'Санкт-Петербург'))
    l = search_users(2, 18, 40, 'Санкт-Петербург')
    pprint(get_photo(41680215))
    lst_asd = get_photo(41680215)
    pprint(sort_photo(lst_asd))

    create_json(l)
