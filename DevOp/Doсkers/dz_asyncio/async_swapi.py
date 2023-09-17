import asyncio # для запуска асинхронного
import datetime # для получения времени

import aiohttp # для корректно отправки запросов http

from more_itertools import chunked # генератор для разбивки запросов по количеству


#импортируем нужное
from model import Base, SwapiInfo, engine, Session

CHUNK_SIZE = 5 # задаем параметр разделения количества запросов

#создаем синхронную функцию запросов
async def get_people(client, people_id):
    #делаем запрос https://swapi.dev/api/people/ < https://swapi.py4e.com/api/people/
    response = await client.get(f'https://swapi.py4e.com/api/people/{people_id}')
    #получаем ответ в формате json
    json_data = await response.json()
    return json_data # возвращаем json

#делаем корректные запросы
async def get_info(urls):
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_all(session, urls)
        return htmls




async def fetch(session, url):
    async with session.get(url) as response:
        if response.status != 200: # не соответствует-ок
            response.raise_for_status() # возвращает объект HTTPError
        return await response.json() # возвращаем json




async def fetch_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results



# записываем в базу данных по ячейкам вызвав insert_to_db из main
async def insert_to_db(results):
    async with Session() as session:
        info_list = [] # создаем словарь для заполнения jsonОМ
        for info_json in results: # перебираем результат
            if info_json.get('url'): # если в info_json есть -url

                # записываем это в переменные, чтобы записать в таблицу
                films = await get_info(info_json.get('films'))
                homeworld = await get_info([info_json.get('homeworld')])
                species =  await get_info(info_json.get('species'))
                starships = await get_info(info_json.get('starships'))
                vehicles = await get_info(info_json.get('vehicles'))

                # "вызываем" таблицу и заполняем ее
                star_war = SwapiInfo (
                    id = int(info_json.get('url')[34:-1]),
                    birth_year = info_json.get('birth_year'),
                    eye_color = info_json.get('eye_color'),
                    films = ', '.join([film.get('title') for film in films]),
                    gender = info_json.get('gender'),
                    hair_color = info_json.get('hair_color'),
                    height = info_json.get('height'),
                    homeworld = homeworld[0].get('name'),
                    mass = info_json.get('mass'),
                    name = info_json.get('name'),
                    skin_color = info_json.get('skin_color'),
                    species = ', '.join([specie.get('name') for specie in species]),
                    starships = ', '.join([starship.get('name') for starship in starships]),
                    vehicles = ', '.join([vehicle.get('name') for vehicle in vehicles]),
                )
                info_list.append(star_war) #добовляем в список
        session.add_all(info_list) # в сессию
        await session.commit() # коммитим





async def main():
    async with engine.begin() as con: # выдергиваем подключения из engine
        await con.run_sync(Base.metadata.drop_all)#удаляем старые таблицы
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all) # создаем таблици
    async with aiohttp.ClientSession() as client: # делаем корректный запрос
        # делаем циклом с запросом нужным по количеству (5)
        for ids_chunk in chunked(range(1, 84), CHUNK_SIZE):
        # Компрехенджен выражение (вместо циклов и пустых списков
            coros = [get_people(client, i) for i in ids_chunk]
#Возвращаем карутину и не ожидаем окончания обработки, не блокируем следующие
            results = await asyncio.gather(*coros)
            #создаем карутину не await
            insert_to_db_coro = insert_to_db(results)
            asyncio.create_task(insert_to_db_coro)
    current_task = asyncio.current_task()
    tasks_to_await = asyncio.all_tasks() - { #Функция задач
            current_task,
    }
    for task in tasks_to_await:  # циклом делаем await всех задач
        await task



if __name__ == "__main__":
    start = datetime.datetime.now()
    asyncio.run(main()) #для запуска карутина main используем asyncio
    print(f'Выполнено за - {datetime.datetime.now() - start}')


