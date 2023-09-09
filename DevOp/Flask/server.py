from flask import Flask, jsonify, request
from flask.views import MethodView #для управления пользователями
from hashlib import md5 # используется для шифровки пароля
from pydantic import ValidationError
from models import User, Session # импортируем из models
from schema import CreateUser, UpdateUser
from sqlalchemy.exc import IntegrityError #исключение
import json

app = Flask('app') # запускаем приложение flask
SALT = 'jkdsbsdkelfjnwkbvsdjfsd' #ее можно добавлять к паролю


class HttpError(Exception): #класс ошибок
    def __init__(self, status_code: int, message: dict | str | list):
        self.status_code = status_code
        self.message = message


def validate(json_data, schema): # делаем функцию валидации
    try:
        model = schema(**json_data)
        return model.dict(exclude_none=True) # возвращаем данные словарем,
        # (чтобы не было пустых полей)
    except ValidationError as err:
        error_message = json.loads(err.json())
        raise HttpError(400, error_message) # запускаем функцию ошибок


@app.errorhandler(HttpError) # регистрируем приожение
def error_handler(er: HttpError): #создаем функцию получение ошибки
    http_response = jsonify({'status': 'error', 'message': er.message})
    http_response.status_code = er.status_code
    return http_response #?


def hash_password(password:str): #создаем для шифровки пароля
    password = f'{SALT}{password}' # для усложнения пароля
    password = password.encode() #перехватываем пароль
    password = md5(password).hexdigest() #шифруем пароль
    return password #возвращаем пароль, но уже шифрованный

# def hello_world():
#
#     return jsonify({"hello":'world'})
#
# app.add_url_rule('/hello/', #  добовляем url
#                  view_func=hello_world,
#                  methods=['get']) # если метот get - запрос тоже должен быть get

def get_user(user_id, session: Session):
    user = session.get(User, user_id)
    if user is None:
        raise HttpError(404, 'user not found')
    return user


class UsersView(MethodView): # Работа с пользователями
    def get(self, users_id):
        with Session() as session:
            user =  get_user(users_id, session)
            return jsonify({
                'id': user.id,
                'name': user.name
            })

    def post(self):
        json_data = validate(request.json, CreateUser)
        #получаем данные от пользователя в json b передаем схему валидации
        json_data['password'] = hash_password(json_data['password'])
    #вызываем функцию, для шифрования пароля
        with Session() as session: # открываем сессию
            new_user = User(**json_data) # создается экземпляр класса user
            session.add(new_user) # добавляем пользователя в сессию
            try:
                session.commit() # сохраняем изменения
            except IntegrityError: # при возникновении ошибки
                raise HttpError(408, 'user already exists')
            return jsonify({    # возвращаем новому пользователю его ID
                'id': new_user.id
            })


    def patch(self, users_id):
        json_data = validate(request.json, UpdateUser)
        if 'password' in json_data:
            json_data['password'] = hash_password(json_data['password'])
        with Session() as session:
            user = get_user(users_id, session)
            for key, value in json_data.items():
                setattr(user, key, value)
            session.add(user)
            try:
                session.commit() # сохраняем изменения
            except IntegrityError: # при возникновении ошибки
                raise HttpError(408, 'user already exists')
            session.commit()
            return jsonify({
                'status': "success"
            })

    def delete(self, users_id): #  удаление пользователя
        with Session() as session:
            user = get_user(users_id, session)
            session.delete(user)
            session.commit()
        return jsonify({
            'status': "success"
        })

user_view = UsersView.as_view('users')  # преобразуем класс во вью и привяжем к методам
app.add_url_rule('/users/<int:users_id>',
                 view_func=user_view,
                 methods=["GET", "PATH", 'DELETE']) #url с id
app.add_url_rule('/users/',
                 view_func=user_view,
                 methods=['POST'] ) # url без id




if __name__ == '__main__':
    app.run()