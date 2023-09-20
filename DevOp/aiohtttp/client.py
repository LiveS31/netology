import asyncio

import aiohttp

# создаем для отправки запросов на сервер

async def main():
    async with aiohttp.ClientSession() as session: # Клиенская сессия
        #Создаем пользователя
        response = await session.post(  #запрос по адресу
            "http://127.0.0.1:8080/user/", #если ?key_1=value_1 -ключ, значение
            json={"name": "user_4", "password": '1234'} # передаем json
        )
        #получаем пользователя
        data = await response.json()
        print(data)
        response = await session.get(
            "http://127.0.0.1:8080/user/5/",

        )
        data = await response.json()
        print(data)

        # response = await session.patch(
        #     "http://127.0.0.1:8080/user/1/",
        #     json={"name": "user_3"}
        # )
        # data = await response.json()
        # print(data)
        #
        # response = await session.get(
        #     "http://127.0.0.1:8080/user/1/",
        #
        # )
        # data = await response.json()
        # print(data)

        # response = await session.delete(
        #     "http://127.0.0.1:8080/user/1/",
        # )
        # data = await response.json()
        # print(data)
        #
        # response = await session.get(
        #     "http://127.0.0.1:8080/user/1/",
        #
        # )
        # data = await response.json()
        # print(data)


asyncio.run(main())
