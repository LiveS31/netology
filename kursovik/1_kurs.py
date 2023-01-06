# Написать программу, которая будет:
#
# Получать фотографии с профиля. Для этого нужно использовать метод photos.get.- ok
# Сохранять фотографии максимального размера(ширина/высота в пикселях) на Я.Диске - ок
# Для имени фотографий использовать количество лайков. -ок
# Сохранять информацию по фотографиям в json-файл с результатами.- ок

# формитруем токен
token_vk = ''
tokenn = ''
import requests #импортируем библиотеку для отправки запросов
import json # для записи в файл
info,url, name, size = [],[],[],[] #для записи переменных
class VK:# создаем класс для оптимизации достука к vk
    def __init__(self, token_vk, owner_id, version='5.131'):
        self.token= token_vk #записываем токен
        self.owner_id = owner_id # пользователя
        self.version = version #
        self.params = {        # записываем все в параметры, чтобы вызывать одной переменной
            'access_token': self.token,
            "album_id": 'profile',
            'owner_id': self.owner_id,
            'v': self.version,
            "photo_sizes": 1,
            "extended": 1,
            'rev':0
        }


    def photos(self): #записываем функцию, чтобы получить доступ к фото пользователя
        url_ = 'https://api.vk.com/method/photos.get'
        res = requests.get(url_,params= {**self.params}).json()
        if 'error' in res: #если есть ошибка (отличие от того что нам нужно) - далее не выполняется
            print (f'Ошибка!!!\n'
                    f'Возможно приватный статус у пользователя id_{self.owner_id}!\n'
                    f'Попробуйте другого!!!')
        else:
            countrs = res['response']['count'] #узнаем сколько будет фоток
            for a in range(countrs): #получаем последнюю фотку с последним описанием
                irl = res['response']['items'][a] #общая у всех
                name.append(irl['likes']['count'])
                size.append(irl['sizes'][-1]['type'])
                url.append(irl['sizes'][-1]['url'])
            print("Список создан... \nДанные переданы далее...")
            ya = Yadisk(tokenn) #передаем на запуск яндекса
            ya.create_folder() #создаем папку(меньше мусора убирать)
            for i in range(len(name)): # циклом копируем картинки на диск
                ya.load_from_internet(url[i], name[i])
                #добавляем в словарь, для записи в файл
                info.append({'file_name': str(name[i]) + '.jpg', 'size': size[i], 'url': url[i]})
            with open('total.txt', 'a', encoding='utf-8') as rec: #записываем
                rec.write(f'Данные пользователя: {self.owner_id}\nКоличество фото пользователя: {len(name)}\n')
                json.dump(info, rec) #записываем json
                rec.write('\n')
            return

#создаем папку на ya_disk для загрузок данных c vk (папка - просто так удобней потом удалить)
class Yadisk:
    def __init__(self, token_ya):
        self.token_ya = token_ya
        self.host = 'https://cloud-api.yandex.net/v1/disk/resources/'

    def key_token(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token_ya}'}
    def create_folder(self):
        params = {'path': '/VK'}
        response = requests.put(self.host, headers=self.key_token(), params=params)
        if response.status_code == 201:
            print (f'Папка VK на YaDisk успешно создана...\nБудет загружено {len(name)} фото.')
        elif response.status_code == 409:
            print (f'Данная папка уже была создана ранее на ресурсе YaDisk.\nБудет загружено {len(name)} фото')
        else:
            print('Ошибка создания папки на YaDisk')
        return

    def load_from_internet(self, file_url, file_name):
        uri = 'upload'  #индификатор пути запроса
        url = self.host+uri  # полный путь для получения действия (запроса)
        params = {'path': f'/VK/{file_name}.jpg', 'url': file_url} #передаем имя и путь
        response = requests.post(url, headers=self.key_token(), params=params)
        if response.status_code == 202:
            print('Загрузка фото прошла успешно')

vk = VK(token_vk , int(input('Введите id пользователя:')))
vk.photos()
