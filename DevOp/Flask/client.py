import requests


response = requests.get('http://127.0.0.1:5000/user/') #  делаем запрос по адресу
print(response.status_code) # выводим статус
print((response.text)) # выводим текст