import requests
import json
import os


#странная какая то фигня. на работе работает, дома нет.... :( хотя сайт открывается
intelligence = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0} #создаем словарь с героями и значениями 0
#задаем переменную URL с сайтом и переборкой с адресом сайта, с внесением параметров в словарь
url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'

heroes_list = ['Hulk', 'Captain america', 'Thanos'] #создаем список с героями для перепорки
for hero in heroes_list: # цикл с переборкой героем заданный списком
    heros_dict = json.loads(requests.get(url + hero).content) #получаем словарь с сайта с помощью json
    # в цикле меняем словарь параметры героев (от нуля)
    intelligence[hero] = int(heros_dict['results'][0]['powerstats']['intelligence'])

print (max(intelligence))# выводим героя с максимальным значением


#2
current = os.getcwd()
folder = "http_requests"
files= 'file.txt'
file = (os.path.abspath(files))
class YaUploader:
    host = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):  # создаем функцию для авторизации. будем авторизовываться через заголовки
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def loading(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        # Тут ваша логика
        url = self.host #прописываем фактически адрес
        params = {'path': f'/{file_path}'}# прописываем имя файла на диске
        response = requests.get(url, headers=self.get_headers(), params=params) #передаем параметры для передачи
        return response.json()['href'] # передаем функцию
    def upload(self,load_file):
        load_link = self.loading(load_file) #создаем переменную для ссылки и передаем туда имя файла на диске
        response = requests.put(load_link, headers=self.get_headers(), data=open(os.path.abspath(load_file), 'rb'))# записываем файл на диск
        print (response.status_code)
        if response.status_code ==201:
            print('Файл успешно загружен!!!')

#выбор пути файла
#вот так это смотрится
print ( os.path.join(current, files))
print (os.path.abspath(files))
print (file)
if __name__ == '__main__':
    #получить токен к загрузке
    path_to_file = '1file.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)




