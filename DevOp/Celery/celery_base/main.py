import datetime
from tasks import cpu_bound



# это от сюда убираем в tasks
# import time

# def cpu_bound(a, b):
#     time.sleep(1)
#     return a + b

def main():
# если к cpu_bound добавить delay - то он создаст задачу для redisОН
    a_task = cpu_bound.delay(3,4) # создаем задачи
    b_task = cpu_bound.delay(9, 4)
    c_task = cpu_bound.delay(8, 4)
    d_task = cpu_bound.delay(4, 4)
    a = a_task.get()
    b = b_task.get()
    c = c_task.get()
    d = d_task.get()

#полный путь запуска celery -A tasks.app worker
#где app - это приложение
#tasks - файл нде оно лежит
#worker - тот что заставляет приложение работать

    print(a, b, c, d)

start = datetime.datetime.now() #засекаем время
main()
print(datetime.datetime.now() - start) # выводим засеченное время