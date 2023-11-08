#тут будут словари с данными
#устанавливаем библиотеку celery, redis

import time
import celery # импортируем celery

app = celery.Celery( #создаем экземпляр класса celery
    broker='redis://127.0.0.1:6379/1', #обращаемся к локальному адресу
    # /1 - это номер базы (по умолчанию, есть несколько количество баз,
    # которые можно использовать)
    backend='redis://127.0.0.1:6379/2'
)

@app.task # превращаем функцию в задачу celary декоратора app.task
def cpu_bound(a, b):
    time.sleep(1)
    return a + b
