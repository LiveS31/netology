# сделать запрос в ВК
import json
# получаем токен из файла
import requests
import configparser
config =configparser.ConfigParser()
config.read('.pass.ini')
#token_vk = config['vk']['KEY_GROUP']
token_vk = config['vk']['TOKEN_VK']

class VK: #создаем класс вк с  нужными пераметрами
    def __init__(self, token_vk, user_id, version='5.131' ):
        self.token = token_vk
        self.version = version
        self.user_id = user_id
        self.params = {'access_token': token_vk,
                  'user_ids': user_id,
                  'fields': 'sex',
                  'v': '5.131'}

        print (self.params)
    def answe(self):

        url_ = 'https://api.vk.com/method/'
        res = requests.get(url_+'database.getCities', params={**self.params}).json()
        print(res)





if __name__=='__main__':
    vk = VK(token_vk, 11)
    vk.answe()
