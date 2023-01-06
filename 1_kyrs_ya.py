url_vk = 'https://sun9-2.userapi.com/c9609/u00019/-6/w_59310eda.jpg'
likes_vk = 5199
site_vk ='w'
token_ya = 'y0_AgAAAAAj1FzIAADLWwAAAADW5Met37_w5V2cRH-vOQKHGD0W0UwaRwY'
import requests
import json
class Yandex:
    host ='https://cloud-api.yandex.net/' #хост яндекса (он не меняется)
    def __init__(self, token): #инициализируем класс и передаем параметр token
        self.token = token # присваиваем токен

    def get_headers(self): #создаем функцию для авторизации. будем авторизоваться через заголовки
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'} #выбираем тип и передаем ключ (self)

#получение данных с ya.disk обязательные параметры выделены черным

    def get_files_list (self): #функция создания списков файлов
        uri = 'v1/disk/resources/files/' #индификатор пути запроса
        url = self.host+uri #полный путь для получения действия (запроса)
        headers = self.get_headers() #получаем заголовки
        params = {'limit':1, 'media_type': 'image'} # создаем словарь с параметрами. (название можно взять из яндекса)
        response = requests.get(url, headers=headers, params=params) #запрос по адресу, передаем параметры
        print(response.json()) #вывод сообщения на экран (в качестве словаря)
        print (response.status_code) #вывод статуса завершения


#создание файла на яндекс диске обязательные параметры выделены черным
    def create_folder(self):
        uri = 'v1/disk/resources/' #индификатор пути запроса
        url = self.host + uri #полный путь для получения действия (запроса)
        params = {'path': '/vk'}
        response = requests.put(url, headers=self.get_headers(), params=params)#put - запрос для передачи
        #headers = headers (так же равно) = headers = self.get_headers()
        #print (response.json())  # вывод сообщения на экран (в качестве словаря)
        print (response.status_code)  # вывод статуса завершения


# загрузка файла с компьютера
    #загружается двумя методами 1. получения ссылки 2 загрузка
    def get_upload_link(self, disk_file_name):# disk_file_name - чтобы можно было менять имя
        uri = 'v1/disk/resources/upload'  #индификатор пути запроса
        url = self.host + uri  # полный путь для получения действия (запроса)
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
        url = self.host+uri  # полный путь для получения действия (запроса)
        #передаем параметры куда загружать и как будет называться фаил
        params = {'path': f'/vk/{file_name}', 'url': file_url}
        #указываем  параметры и куда положить
        response = requests.post(url, headers=self.get_headers(), params=params)
        print(response.status_code)  # вывод статуса завершения
        if response.status_code == 202:
            print('Загрузка прошла успешно')

# ya = Yandex(token_ya) # передать переменной ya
#ya.get_files_list() #запустить код получение данных с ya.disk
#ya.create_folder() #запустить код создания папки на ya.disk
#ya.get_upload_link('date.json') #проверка получения получено url
#ya.get_upload_from_pc('test.json', 'file.json') # указываем для записи название на pc и как называться будет на ya
# file_url= url_vk#'https://www.kartinki24.ru/uploads/gallery/thumb/25/kartinki24_ru_love_103.jpg'
# ya.load_from_internet(file_url,'1.jpeg') # название переменной url и название фал как будет называться на дискеloadingloadingloading

with open('total.txt', 'a', encoding='utf-8') as rec:
    rec.write('kdfggf lg')
