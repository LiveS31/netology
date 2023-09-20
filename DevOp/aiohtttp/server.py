import json

from aiohttp import web
from bcrypt import checkpw, gensalt, hashpw #библиотека шифрования
# gensalt - генерация sold
# hashpw - хешировать пароль
# checkpw - проверить пароль

from sqlalchemy.exc import IntegrityError # импортируем

from model import Base, Session, User, engine


# функция хеширования пароля
def hash_password(password: str): #принимаем пароль в строковом виде
    password = password.encode() #преобразовываем в байты
    password = hashpw(password, gensalt()) # хешируем (первым аргуметом пароль, вторым соль
    password = password.decode() # полученный пароль превращаем обратно в строчку
    return password # возвращаем



#Проверка пароля
def check_password(password: str, hashed_password: str): #ожидаем, что
    # в базе лежит обычный пароль, а клиент присылает обычный
    password = password.encode() # преобразуем обычный пароль в байты
    hashed_password = hashed_password.encode() # преобразует хешированный пароль в байты
    return checkpw(password, hashed_password) # выполняем метод check password

#делаем функцию, чтобы не копипастить код
def get_http_error(http_error_class, message): # принимаем класс ошибки которую хотим создать и сообщение
    return http_error_class( #возвращать буем сообщение об ошибке (http_error_class- переменная)
        text=json.dumps({"error": message}), content_type="application/json")



app = web.Application() #Создаем класс апликацион

#делаем клинап контексты для выполнения кода
# на старте приложения и завершении его работы
async def orm_cntx(app: web.Application):  #асинхронная функция принимает
    # на вход приложение (app: web.Application)
    print("START") #информативное сообщение
    async with engine.begin() as con: #  подключаемся к базе данных
        # (выдергивая подключение из engine)
        #await con.run_sync(Base.metadata.drop_all) # удаляем базу данных
        await con.run_sync(Base.metadata.create_all) # создаем базу данных

# то что написано до yield - выполнится во время старта приложения
    yield # - это ключевое слово
# то что напишем после yield - выполнится при завершении работы приложения


    await engine.dispose() # отключаемся от базы данных
    print("SHUT DOWN")#информативное сообщение


@web.middleware #данную функцию регистрируем как middleware
#для этого ее декорируем декоратором


#нужна для открытия и закрытия сессии
async def session_middleware(request: web.Request, handler):
    #принимает два аргумента web.Request, handler-функция которая обрабатывает request
    #(post, path, get....)

    async with Session() as session: # открываем асинхронную ссессию
        request["session"] = session # кладем ссессию в объект request (работает как словарь)
        response = await handler(request)# выполняем REQUEST
        return response # возвращаем ответ

#регистрируем контекст
app.cleanup_ctx.append(orm_cntx) # список который можно append добавлять
app.middlewares.append(session_middleware) #добовляем аппендом написанную функцию


#асинхронная функция, принимает user_id, session.
#экземпляк класса USER
async def get_user(user_id: int, session: Session) -> User:
    user = await session.get(User, user_id) # получаем id
    if user is None: # если юзера нет
        raise get_http_error(web.HTTPNotFound, "user not found")
        #Возвращаем ошибку. web.HTTPNotFound - пред подготовленный статус
    return user #возвращаем пользователя


class UserView(web.View): # создаем вьеху от класса web.View
    @property #метим функцию декоратором
    def session(self) -> Session: # возвращает сессию из request
# -> Session - указывает, что возвращает экземпляры класса сессии
        return self.request["session"] #возврат результата

    @property
    def user_id(self) -> int:
        return int(self.request.match_info["user_id"])
    # match_info - падают все переменные в rout

    async def get(self):
        user = await get_user(self.user_id, self.session) #делаем запрос
        return web.json_response( #выводим пользователю информацию в JSON
            {
                "id": user.id,
                "name": user.name,
                "creation_time": user.creation_time.isoformat(), #время создания в формате строчки
            }
        )

    async def post(self):
        json_data = await self.request.json() #извлекаем json
        #Валидируем данные и подменяем пароль на захешированный
        json_data["password"] = hash_password(json_data["password"])
        user = User(**json_data) #создаем экземпляр класса юзер
        try:
            self.session.add(user) #добовляем юзера в сессию
            await self.session.commit() # коммитим
            # IntegrityError импортируем из sqlalchemy.exc
        except IntegrityError as err: # если нет уникальности юзера получим ошибку
            #Выводим пользовтелю ошибку - конфликт web.HTTPConflict
            raise get_http_error(web.HTTPConflict, "user already exists")
        return web.json_response({"id": user.id}) # возвращаем json

    async def patch(self):
        json_data = await self.request.json()  #извлекаем json
        if "password" in json_data: # если password присутствует
            # Валидируем данные и подменяем пароль на захешированный
            json_data["password"] = hash_password(json_data["password"])

        user = await get_user(self.user_id, self.session) # Получаем пользователя
        for key, value in json_data.items(): # перебираем словарь (патчим юзера)
            setattr(user, key, value) #устанавливаем соответствущие атрибуты у пользователя
        try:
            self.session.add(user)
            await self.session.commit()
        except IntegrityError as err:
            raise get_http_error(web.HTTPConflict, "user already exists")
        return web.json_response({"id": user.id})

    async def delete(self):
        #получаем пользователя
        user = await get_user(self.user_id, self.session)
        #вызываем синхронный метод сейшан делит
        await self.session.delete(user)
        #асинхронный метод коммит
        await self.session.commit()
        #Возвращаем результат
        return web.json_response({"status": "deleted"})


app.add_routes( #добовляем rout для указания пути к нужному "отображению"
    # route передается списком для возможности добавления множества rout
    [
        web.get("/user/{user_id:\d+}/", UserView),
        # Передаем user_id, который хоти получить из базы.
        # регулярка которая отвечает за любое количетво цифрофых символов  :\d+
        web.patch("/user/{user_id:\d+}/", UserView),
        # передаем сюда класс UserView
        web.delete("/user/{user_id:\d+}/", UserView),
        web.post("/user/", UserView), # так как клиент не знает id,
        # которое будет создавать - не будем передавать
    ]
)

if __name__ == "__main__": #запуск app
    web.run_app(app)
