import datetime

import requests


def get_people(people_id): # функция
    #возвращает запрос отправленный на адрес с запросом people_id, которой возвращает json
    return requests.get(f"https://swapi.dev/api/people/{people_id}").json()


def main():
    person_1 = get_people(1) # запрос на персонажи
    person_2 = get_people(2) # запрос на персонажи
    person_3 = get_people(3) # запрос на персонажи
    person_4 = get_people(4) # запрос на персонажи
    # Вывод персонажей
    print(person_1, person_2, person_3, person_4)


if __name__ == "__main__":
    start = datetime.datetime.now() #время начала работы
    main() #запуск функции
    print(datetime.datetime.now() - start) #вывод на экран
