import time

import requests

resp = requests.post("http://127.0.0.1:5000/upscale/")
resp_data = resp.json()
print(resp_data)
task_id = resp_data.get("task_id")

status = "PENDING"
while status == "PENDING":
    resp_data = requests.get(f"http://127.0.0.1:5000/tasks/{task_id}/").json()
    status = resp_data.get("status")
    time.sleep(20)
    print(resp_data)

result_file = "lama_600px.png"
# Для получения изображения открыть ссылку в браузере
response = requests.get(f"http://127.0.0.1:5000/processed/{result_file}/")