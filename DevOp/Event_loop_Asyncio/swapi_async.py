import asyncio # для запуска асинхронного main
import datetime

import aiohttp # для корректной отправки запросов.
# Является и клиентом и севром одновременно
# (одновременно замена фласка и реквеста)
from more_itertools import chunked # генератор разбивающий последовательности ни части

from models import Base, Session, SwapiPeople, engine
#импортируем нужное

CHUNK_SIZE = 5 # задаем количество запросов, которые можем обработать


async def get_people(client, people_id):  # синхронная функция пишется с async
    response = await client.get(f"https://swapi.py4e.com/api/people/{people_id}")
    #делаем запрос
    json_data = await response.json() #получаем ответ json
    return json_data # выводим джейсон
# Данная функция не выполняет код сразу. она возвращает специальный обхект - назается корутина
# корутина - предподготовленных запрос, который можно отправить позже)
# для выполнения запроса используется слово await
# корутины можно выполнять только внутри других асинхронных функций



async def insert_to_db(results):
    async with Session() as session:
        swapi_people_list = [SwapiPeople(json=item) for item in results]
        session.add_all(swapi_people_list)
        await session.commit()
#функция выполняет действия в момент создания не действия не блокируя остальные
# остальные корутины в функции main

async def main():
    async with engine.begin() as con: # выдергиваем подключение из engine
        await con.run_sync(Base.metadata.drop_all) # удаляем таблицу
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all) #запускаем код миграции, создаем таблицу
    async with aiohttp.ClientSession() as client:
        for ids_chunk in chunked(range(1, 100), CHUNK_SIZE):
            #Разбиваем последовательность из 5 чисел (как было указано)
            coros = [get_people(client, i) for i in ids_chunk] # Компрехенджен выражение (вместо циклов и пустых списков)
            results = await asyncio.gather(*coros)
    #gather - возвращает карутину, она ожидая отработки предыдущей операции,
    # не блокируют друг - друга. они будут попадать в результат
            insert_to_db_coro = insert_to_db(results) #создаем корутину не await ее
            asyncio.create_task(insert_to_db_coro)
    current_task = asyncio.current_task()
    tasks_to_await = asyncio.all_tasks() - { #Функция задач
        current_task,
    }
    for task in tasks_to_await: # циклом делаем await всех задач
        await task


if __name__ == "__main__":
    start = datetime.datetime.now()
    asyncio.run(main()) #для запуска карутина main используем asyncio
    print(datetime.datetime.now() - start)
