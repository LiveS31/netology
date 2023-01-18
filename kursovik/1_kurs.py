# Написать программу, которая будет:
#
# Получать фотографии с профиля. Для этого нужно использовать метод photos.get.- ok
# Сохранять фотографии максимального размера(ширина/высота в пикселях) на Я.Диске - ок
# Для имени фотографий использовать количество лайков. -ок
# Сохранять информацию по фотографиям в json-файл с результатами.- ок
# Токен из файла - ок (new)
# Получить screen_name - ok(new)
# передать id из screen_name в self.owner_id - ок (new)
# добавлять дату для фото с одинаковыми лайками -ok
# избавиться от глобальных переменных -ok
# дублирующие фото + дата - ок
# запись по json - ok
# выбор количества фото - ок
# забираем токены (думал, что в данном случае лучше оставить как было)

import configparser
import json
import requests
config = configparser.ConfigParser()
config.read("code.ini")
token_vk = config['code']['VKT']
tokenn = config['code']['YAAPI']

class VK:# создаем класс для оптимизации доступа к vk
    def __init__(self, token, user_ids , version='5.131'):
        self.token = token #записываем токен
        self.version = version
        self.user_ids = user_ids
        self.params = {      # записываем все в параметры, чтобы вызывать одной переменной
            'access_token': self.token,
            "album_id": 'profile',
            'v': self.version,
            "photo_sizes": 1,
            "extended": 1,
            'rev': 0,
            'user_ids': self.user_ids
        }

    def photos(self): #записываем функцию, чтобы получить доступ к фото пользователя
        data_foto = []
        url = []
        info = []
        name = []
        size = []
        url_ = 'https://api.vk.com/method/'
        res1 = requests.get(url_+'users.get', params={**self.params}).json()
        if 'error' in res1:
            print('Ошибка токена!!!', res1['error']['error_msg'], sep='\n')
        elif res1['response'] == [ ]:
            print(f'Пользователь {self.user_ids} не найден!!!')
        else:
            self.params['owner_id'] = res1['response'][0]['id']
            res = requests.get(url_+'photos.get', params={**self.params}).json()
            if 'error' in res: #если есть ошибка (отличие от того что нам нужно) - далее не выполняется
                print(f'Ошибка!!!\n'
                        f'Возможно приватный статус у пользователя id_{self.user_ids}!\n'
                        f'Попробуйте другого!!!')
            else:
                countrs = res['response']['count'] #узнаем сколько будет фоток
                for a in range(countrs): #получаем последнюю фотку с последним описанием
                    irl = res['response']['items'][a] #общая у всех
                    data_foto.append(irl['date'])
                    name.append(irl['likes']['count'])
                    size.append(irl['sizes'][-1]['type'])
                    url.append(irl['sizes'][-1]['url'])
                print(f'Список фотографий пользователя {self.user_ids} всего из {len(name)} шт создан... '
                      f'\nДанные переданы далее...')

                while True:
                    sum_foto = int(input(f'Введите количество загружаемых фото (от 0 до {len(name)}): '))
                    if 0 <= sum_foto <= (len(name)):
                        break

                ya = Yadisk(tokenn)
                ya.create_folder(self.user_ids, name, sum_foto)

                re_name = [*set(name)]
                for i in range (sum_foto):
                    if name[i] in re_name:
                        re_name.remove(name[i])
                    else:
                        name[i] = str(name[i]) + '_' + str(data_foto[i])

                    ya.load_from_internet(url[i], name[i], self.user_ids)
                        #добавляем в словарь, для записи в файл
                    info.append({'file_name': str(name[i]) + '.jpg', 'size': size[i], 'url': url[i]})

                with open('total.json', 'a', encoding='utf-8') as rec: #открываем
                    json.dump(info, rec, indent=2) #записываем json
                    print("для инфы - файд записан\n Файлы загружены")
                return

#создаем папку на ya_disk для загрузок данных c vk (папка - просто так удобней потом удалить)
class Yadisk:
    def __init__(self, token_ya):
        self.token_ya = token_ya
        self.host = 'https://cloud-api.yandex.net/v1/disk/resources/'
    def key_token(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token_ya}'}
    def create_folder(self, id_us, name, sum_foto):
        params = {'path': f'/VK/'}
        response = requests.put(self.host, headers=self.key_token(), params=params)
        params = {'path': f'/VK/{id_us}'}
        response = requests.put(self.host, headers=self.key_token(), params=params)

        if response.status_code == 201:
            print(f'Папка VK на YaDisk успешно создана...'
                   f'\nБудет загружено {sum_foto} из {len(name)} фото.')
        elif response.status_code == 409:
            print(f'Данная папка уже была создана ранее на ресурсе YaDisk.'
                   f'\nБудет загружено {sum_foto} из {len(name)} фото')
        else:
            print('Ошибка создания папки на YaDisk')
        return

    def load_from_internet(self, file_url, file_name, id_us):
        uri = 'upload'  #индификатор пути запроса
        url = self.host+uri  # полный путь для получения действия (запроса)
        params = {'path': f'/VK/{id_us}/{file_name}.jpg', 'url': file_url}
        response = requests.post(url, headers=self.key_token(), params=params)
        if response.status_code == 202:
            print('Загрузка фото прошла успешно')

if __name__ == '__main__':
    vk = VK(token_vk ,(input('Введите id или screen_name пользователя:')))
    vk.photos()


