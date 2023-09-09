#создаем схему валидности (проверки) пароля
#pip install pydantic - применяется для установки валидации
from pydantic import BaseModel, validator
# BaseModel - базовая модель валидации
# validators - обеспечивает дополнительную валидацию
from typing import Optional # чтобы сделать пароль опциональным



class CreateUser(BaseModel): #создаем класс валидаии
    name: str # ожидаем от клиента имя
    password: str # ожидаем пароль


    @validator('password')
    def secure_password(cls, value):
# проверяем пароль на валидность
        if len(value) <= 8: # если длинна пароля меньше 8
            raise ValueError('Password is short') # возвращаем ошибку - пароль короткий
            return value

class UpdateUser(BaseModel):  # создаем класс валидаии
    name: Optional[str]  # ожидаем от клиента имя (с функцией opcional)
    password: Optional[str]  # ожидаем пароль (с функцией opcional)

    @validator('password')
    def secure_password(cls, value):
        # проверяем пароль на валидность
        if len(value) <= 8:  # если длинна пароля меньше 8
            raise ValueError('Password is short')  # возвращаем ошибку - пароль короткий
