 #получене данных от сайта
import requests
# url = 'http://google.com'
#
# response = requests.get(url)
# print (f'Заголовки {response.headers}') #преобразует в словарь
# print (f'контент {response.content}')
# print (f'Текст {response.text}')
# print (f'{response.json}')
# print (f'Статус {response.status_code}')

#yadisk работа с диском

#TOKEN = '' #- токн яндес
#создаем другой файл py . переносим туда ключ, далле импортируем его
from sett import TOKEN #импортируем токен из другого файла

# получение списка файлов
# Создание папки
# загрузка файла с компьютера
# загрузка файла из интернета

# так как действия они имеют одинаковые - обЪединим в класс
class Yandex:
    host ='https://cloud-api.yandex.net/' #хост яндекса (он не меняется)
    def __init__(self, token): #инициализируем класс и передаем параметр token
        self.token = token # присваиваем токен

    def get_headers(self): #создаем функцию для авторизации. будем авторизовываться через заголовки
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'} #выбираем тип и передаем ключ (self)

#получение данных с ya.disk обязательные параметры выделены черным

    def get_files_list (self): #функция создания списков файлов
        uri = 'v1/disk/resources/files/' #индификатор пути запроса
        url = self.host+uri #полный путь для получения действыия (запроса)
        headers = self.get_headers() #получаем заголови
        params = {'limit':1, 'media_type': 'image'} # создаем словарь с параметрами. (название можно взять из яндекса)
        response = requests.get(url, headers=headers, params=params) #запрос по адресу, передаем параметры
        print(response.json()) #вывод сообщения на экран (в качестве словаря)
        print (response.status_code) #вывод статуса завершения


#создание файла на яндекс диске обязательные параметры выделены черным
    def create_folder(self):
        uri = 'v1/disk/resources/' #индификатор пути запроса
        url = self.host + uri #полный путь для получения действыия (запроса)
        params = {'path': '/test_folder'}
        response = requests.put(url, headers=self.get_headers(), params=params)#put - запрос для передачи
        #headers = headers (так же равно) = headers = self.get_headers()
        print (response.json())  # вывод сообщения на экран (в качестве словаря)
        print (response.status_code)  # вывод статуса завершения


# загрузка файла с компьютера
    #загружается двумя методами 1. получения ссылкиб 2 загрузка
    def get_upload_link(self, disk_file_name):# disk_file_name - чтобы можно было менять имя
        uri = 'v1/disk/resources/upload'  #индификатор пути запроса
        url = self.host + uri  # полный путь для получения действыия (запроса)
        # #указываются путь куда будет загрузка и под каким именем загрузится файл
        params = {'path': f'/{disk_file_name}'}   #'/test_folder/data.json')
        # передаем параметры для получения ссылки на загрузку
        response = requests.get(url, headers=self.get_headers(), params=params)
        print(response.json())  # вывод сообщения на экран (в качестве словаря)
        print(response.status_code)  # вывод статуса завершения
        return response.json()['href'] # для передачи данных метода дальше (на запись в данном случае)

# после получения ссылки
    #один параметр как называется файл на компе, другой как будет на диске
    def get_upload_from_pc(self, local_file_name, disk_file_name):
        #получаем ссылку +передаем название файла на диске
        upload_link = self.get_upload_link(disk_file_name)
        # передаем ссылкой файл на загрузку #dаta - это тело запроса
        response = requests.put(upload_link, headers=self.get_headers(), data=open(local_file_name, 'rb'))
        print(response.status_code)  # вывод статуса завершения
        if response.status_code ==201:
            print  ('Загрузка прошла успешно')


# загрузка файла из интернета
    def load_from_internet(self, file_url, file_name):
        uri = 'v1/disk/resources/upload'  #индификатор пути запроса
        url = self.host+uri  # полный путь для получения действыия (запроса)
        #передаем параметры куда загружать и как будет называться фаил
        params = {'path': f'/test_folder/{file_name}', 'url': file_url}
        #указываем  параметры и куда положить
        response = requests.post(url, headers=self.get_headers(), params=params)
        print(response.status_code)  # вывод статуса завершения
        if response.status_code == 202:
            print('Загрузка прошла успешно')




ya = Yandex(TOKEN) # передать переменной ya
#ya.get_files_list() #запустить код получение данных с ya.disk
#ya.create_folder() #запустить код создания папки на ya.disk
#ya.get_upload_link('date.json') #проверка получения полученно url
ya.get_upload_from_pc('test.json', 'file.json') # указваем для записи название на pc и как называться будет на ya
#file_url='https://www.kartinki24.ru/uploads/gallery/thumb/25/kartinki24_ru_love_103.jpg'
#ya.load_from_internet(file_url,'1.jpeg') # название перееменной url и название фал как будет называться на дискеloadingloadingloading
