#создаем схему валидности (проверки) пароля
#pip install pydantic - применяется для установки валидации

from pydantic import BaseModel, validator
# BaseModel - базовая модель валидации
# validators - обеспечивает дополнительную валидацию
from typing import Optional # чтобы сделать пароль опциональным


class CreateUser(BaseModel): #создаем класс валидации
    name: str # ожидаем от клиента имя
    password: str # ожидаем пароль
    email: str # ожидаем почту

    @validator('password')
    def secure_password(cls, value): # функция валидности
        if len(value) <=8: # проверяем пароль на валидность
            raise ValueError('Password is short!') # возвращаем ошибку - пароль короткий
        return value


class UpdateUser(BaseModel):
    name: Optional[str] # ожидаем от клиента имя (с функцией opcional)
    password: Optional[str]  # ожидаем пароль (с функцией opcional)
    email: Optional[str]  # ожидаем почту (с функцией opcional)

    @validator('password')
    def secure_password(cls, value):
        if len(value) <= 8:
            return ValueError('Password in short!')
        return value
