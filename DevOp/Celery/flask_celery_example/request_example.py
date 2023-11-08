#сравнивам фото отсюда


import requests
import base64
import time


#передаем файла с указанием пути к ним
resp = requests.post('http://127.0.0.1:5000/comparison', files={
    # на этот путь передаем
    'image_1': open('example/valeri_nikolaev.jpg', 'rb'),
    'image_2': open('example/zhan_zhar.jpeg', 'rb')
})
resp_data = resp.json()
print(resp_data)
task_id = resp_data.get('task_id')# сохраняем в отдельную переменную
print(task_id)
#

#выполним get запрос за на тотже саый роут (путь)
resp = requests.get(f'http://127.0.0.1:5000/comparison/{task_id}')
print(resp.json())
time.sleep(3) # слип ставят специально, чтобы сократить колличество запросос

resp = requests.get(f'http://127.0.0.1:5000/comparison/{task_id}')
print(resp.json())