import json

from aiohttp import web
from bcrypt import checkpw, gensalt, hashpw #библиотека шифрования
# gensalt - генерация sold
# hashpw - хешировать пароль
# checkpw - проверить пароль

from sqlalchemy.exc import IntegrityError # импортируем
from model import Session, User, Announcement, engine, Base  # импортируем из model


#SALT = 'jkdsbsdkelfjnwkbvsdjfsd' #ее можно добавлять к паролю

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


app = web.Application() # запускаем приложение flask

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
                "email": user.email, #
            }
        )


    async def post(self):
        json_data = await self.request.json()  # извлекаем json
        # Валидируем данные и подменяем пароль на захешированный
        json_data["password"] = hash_password(json_data["password"])
        user = User(**json_data)  # создаем экземпляр класса юзер
        try:
            self.session.add(user)  # добовляем юзера в сессию
            await self.session.commit()  # коммитим
            # IntegrityError импортируем из sqlalchemy.exc
        except IntegrityError as err:  # если нет уникальности юзера получим ошибку
            # Выводим пользовтелю ошибку - конфликт web.HTTPConflict
            raise get_http_error(web.HTTPConflict, "user already exists")
        return web.json_response({"id": user.id})  # возвращаем json

    async def patch(self):
        json_data = await self.request.json()  # извлекаем json
        if "password" in json_data:  # если password присутствует
            # Валидируем данные и подменяем пароль на захешированный
            json_data["password"] = hash_password(json_data["password"])

        user = await get_user(self.user_id, self.session)  # Получаем пользователя
        for key, value in json_data.items():  # перебираем словарь (патчим юзера)
            setattr(user, key, value)  # устанавливаем соответствущие атрибуты у пользователя
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


async def get_announcement(adv_id: int, session: Session) -> Announcement:
    user = await session.get(Announcement, adv_id)
    if user is None:
        raise get_http_error(web.HTTPNotFound, "advertisement not found")
    return user


class AnnouncementView(web.View):
    @property
    def session(self) -> Session:
        return self.request["session"]

    @property
    def adv_id(self) -> int:
        return int(self.request.match_info["adv_id"])

    async def get(self):
        announcement = await get_announcement(self.adv_id, self.session)
        return web.json_response(
            {
                "id": announcement.id,
                "title": announcement.title,
                "email": announcement.description,
            }
        )

    async def post(self):
        json_data = await self.request.json()
        announcement = Announcement(**json_data)
        self.session.add(announcement)
        await self.session.commit()
        return web.json_response({"id": announcement.id})

    async def patch(self):
        json_data = await self.request.json()
        announcement = await get_announcement(self.adv_id, self.session)
        for key, value in json_data.items():
            setattr(announcement, key, value)
        self.session.add(announcement)
        await self.session.commit()
        return web.json_response({"id": announcement.id})

    async def delete(self):
        announcement = await get_announcement(self.adv_id, self.session)
        await self.session.delete(announcement)
        await self.session.commit()
        return web.json_response({"status": "deleted"})



app.add_routes( #добовляем rout для указания пути к нужному "отображению"
    # route передается списком для возможности добавления множества rout
    [
        web.get("/announcement/{user_id:\d+}/", UserView),
        # Передаем user_id, который хоти получить из базы.
        # регулярка которая отвечает за любое количетво цифрофых символов  :\d+
        web.patch("/announcement/{user_id:\d+}/", UserView),
        # передаем сюда класс UserView
        web.delete("/announcement/{user_id:\d+}/", UserView),
        web.post("/announcement/", UserView), # так как клиент не знает id,
        # которое будет создавать - не будем передавать
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













# class HttpError(Exception): #класс ошибок
#     def __init__(self, status_code: int, message: dict | str | list):
#     # передаем в функцию ошибки
#         self.status_code = status_code #получаем статус ошибки
#         self.message = message # получаем сообщение ошибки
#
#
# @app.errorhandler(HttpError) # регистрируем приожение
# def error_handler(er: HttpError): #создаем функцию получение ошибки
#     http_response = jsonify({'status': 'error', 'message': er.message})
#     # отправляем данные в json
#     http_response.status_code = er.status_code
#     # туда же добавляем
#     return http_response # возвращаем пользователю
#
#
# def get_user(user_id: int, session: Session): #вызываем функцию запроса
#     user = session.get(User, user_id) #записываем в переменную
#     if user is None: # если нет user
#         #выводим сообщение пользователю
#         raise HttpError(404, 'user not found')
#     return user # возвращаем пользователя
#
#
# def get_ann(ann_id: int, session: Session): #вызываем функцию запроса
#     ann = session.get(Announcement, ann_id) #записываем в переменную
#     if ann is None: # если нет ann
#         #выводим сообщение пользователю
#         raise HttpError(404, 'announcement not found')
#     return ann # возвращаем пользователя
#
# def validate(json_data, shema):
#     try:
#         model = shema(**json_data)
#         return model.dict(exclude_none=True)
#     except ValidationError as er:
#         error_message = json.loads(er.json())
#         raise HttpError(400, error_message)
#
#
#
# def hash_password(password:str):
#     password = str(password).encode() # переводим пароль в байты
#     password = md5(password).hexdigest() # шифруем пароль
#     return password # возвращаем в зашифрованном виде
#
# class AnnouncementView(MethodView):
#     def get(self, ann_id):
#         with Session() as session:
#             ann = get_ann(ann_id, session)
#             return jsonify({
#                 'id': ann.id,
#                 'title': ann.title,
#                 'announcement': ann.announcement
#             })
#
#
#     def post(self):
#         with Session as session:
#             new_ann = Announcement(**request.json)
#             session.add(new_ann)
#             session.commit()
#             return jsonify({
#                 'id': new_ann.id
#             })
#
#
#     def patch(self, ann_id):
#         with Session() as session:
#             ann = get_ann(ann_id, session)
#             for key, value in request.json.items():
#                 setattr(ann, key, value)
#             session.add(ann)
#             session.commit()
#             return jsonify({
#                 'status': 'success'
#             })
#
#     def delete(self, ann_id):
#         with Session as session:
#             ann = get_ann(ann_id, session)
#             session.delete(ann)
#             session.commit()
#             return jsonify({
#                 'status': 'success'
#             })
#
#
# def hash_password(password: str):
#     password = str(password).encode()
#     password = md5(password).hexdigest()
#     return password
#
#
# class UsersView(MethodView):
#     def get(self, ann_id):
#         with Session() as session:
#             ann = get_ann(ann_id, session)
#             return jsonify({
#                 'id': ann_id,
#                 'title': ann.title,
#                 'announcement': ann.announcement
#             })
#
#
#     def post(self):
#         json_data = validate(
#             request.json, CreateUser
#         )
#         json_data['password'] = hash_password(json_data['password'])
#         with Session() as sessions:
#             new_ann = User(**json_data)
#             sessions.add(new_ann) #добавляем новое объявление
#             try:
#                 sessions.commit() #сохраняем изменения
#
#             except IndexError:
#                 raise HttpError(408, 'user already exists')
#             return jsonify({'id':new_ann.id})
#
#
#     def patch(self, ann_id):
#         json_data = validate(
#             request.json, UpdateUser
#         )
#         if 'password' in json_data:
#             json_data['password'] = hash_password(json_data['password'])
#         with Session() as session:
#             ann = get_ann(ann_id, session)
#             for key, value in request.json.items():
#                 setattr(ann, key, value)
#             session.add(ann)
#             try:
#                 session.commit()
#             except IndexError:
#                 raise HttpError(408, 'user already exists')
#             return jsonify({'status': 'success'})
#
#
#     def delete(self, user_id):
#         with Session() as session:
#             user = get_user(user_id, session)
#             session.delete(user)
#             session.commit()
#             return jsonify({'status': 'success'})
#
#
# announcement_view = AnnouncementView.as_view("advertisement")
# app.add_url_rule("/advertisements/", view_func=announcement_view, methods=["POST"])
#
# app.add_url_rule(
#     "/advertisements/<int:adv_id>/", view_func=announcement_view, methods=["GET", "PATCH", "DELETE"]
# )
#
# user_view = UsersView.as_view("user")
#
# app.add_url_rule("/users/", view_func=user_view, methods=["POST"])
#
# app.add_url_rule(
#     "/users/<int:user_id>/", view_func=user_view, methods=["GET", "PATCH", "DELETE"]
# )
#
# if __name__ == '__main__':
#     app.run()