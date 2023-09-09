import json
from hashlib import md5  # используется для шифровки пароля

from flask import Flask, jsonify, request
from flask.views import MethodView
from pydantic import ValidationError

from models import Session, User, Announcement  # импортируем из models
from schema import CreateUser, UpdateUser # импортируем из schema

app = Flask('app') # запускаем приложение flask
#SALT = 'jkdsbsdkelfjnwkbvsdjfsd' #ее можно добавлять к паролю


class HttpError(Exception): #класс ошибок
    def __init__(self, status_code: int, message: dict | str | list):
    # передаем в функцию ошибки
        self.status_code = status_code #получаем статус ошибки
        self.message = message # получаем сообщение ошибки


@app.errorhandler(HttpError) # регистрируем приожение
def error_handler(er: HttpError): #создаем функцию получение ошибки
    http_response = jsonify({'status': 'error', 'message': er.message})
    # отправляем данные в json
    http_response.status_code = er.status_code
    # туда же добавляем
    return http_response # возвращаем пользователю


def get_user(user_id: int, session: Session): #вызываем функцию запроса
    user = session.get(User, user_id) #записываем в переменную
    if user is None: # если нет user
        #выводим сообщение пользователю
        raise HttpError(404, 'user not found')
    return user # возвращаем пользователя


def get_ann(ann_id: int, session: Session): #вызываем функцию запроса
    ann = session.get(Announcement, ann_id) #записываем в переменную
    if ann is None: # если нет ann
        #выводим сообщение пользователю
        raise HttpError(404, 'announcement not found')
    return ann # возвращаем пользователя

def validate(json_data, shema):
    try:
        model = shema(**json_data)
        return model.dict(exclude_none=True)
    except ValidationError as er:
        error_message = json.loads(er.json())
        raise HttpError(400, error_message)



def hash_password(password:str):
    password = str(password).encode() # переводим пароль в байты
    password = md5(password).hexdigest() # шифруем пароль
    return password # возвращаем в зашифрованном виде

class AnnouncementView(MethodView):
    def get(self, ann_id):
        with Session() as session:
            ann = get_ann(ann_id, session)
            return jsonify({
                'id': ann.id,
                'title': ann.title,
                'announcement': ann.announcement
            })


    def post(self):
        with Session as session:
            new_ann = Announcement(**request.json)
            session.add(new_ann)
            session.commit()
            return jsonify({
                'id': new_ann.id
            })


    def patch(self, ann_id):
        with Session() as session:
            ann = get_ann(ann_id, session)
            for key, value in request.json.items():
                setattr(ann, key, value)
            session.add(ann)
            session.commit()
            return jsonify({
                'status': 'success'
            })

    def delete(self, ann_id):
        with Session as session:
            ann = get_ann(ann_id, session)
            session.delete(ann)
            session.commit()
            return jsonify({
                'status': 'success'
            })


def hash_password(password: str):
    password = str(password).encode()
    password = md5(password).hexdigest()
    return password


class UsersView(MethodView):
    def get(self, ann_id):
        with Session() as session:
            ann = get_ann(ann_id, session)
            return jsonify({
                'id': ann_id,
                'title': ann.title,
                'announcement': ann.announcement
            })


    def post(self):
        json_data = validate(
            request.json, CreateUser
        )
        json_data['password'] = hash_password(json_data['password'])
        with Session() as sessions:
            new_ann = User(**json_data)
            sessions.add(new_ann) #добавляем новое объявление
            try:
                sessions.commit() #сохраняем изменения

            except IndexError:
                raise HttpError(408, 'user already exists')
            return jsonify({'id':new_ann.id})


    def patch(self, ann_id):
        json_data = validate(
            request.json, UpdateUser
        )
        if 'password' in json_data:
            json_data['password'] = hash_password(json_data['password'])
        with Session() as session:
            ann = get_ann(ann_id, session)
            for key, value in request.json.items():
                setattr(ann, key, value)
            session.add(ann)
            try:
                session.commit()
            except IndexError:
                raise HttpError(408, 'user already exists')
            return jsonify({'status': 'success'})


    def delete(self, user_id):
        with Session() as session:
            user = get_user(user_id, session)
            session.delete(user)
            session.commit()
            return jsonify({'status': 'success'})


announcement_view = AnnouncementView.as_view("advertisement")
app.add_url_rule("/advertisements/", view_func=announcement_view, methods=["POST"])

app.add_url_rule(
    "/advertisements/<int:adv_id>/", view_func=announcement_view, methods=["GET", "PATCH", "DELETE"]
)

user_view = UsersView.as_view("user")

app.add_url_rule("/users/", view_func=user_view, methods=["POST"])

app.add_url_rule(
    "/users/<int:user_id>/", view_func=user_view, methods=["GET", "PATCH", "DELETE"]
)

if __name__ == '__main__':
    app.run()