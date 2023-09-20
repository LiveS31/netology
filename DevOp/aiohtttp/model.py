#делаем подключение к базе

import os

from sqlalchemy import Column, DateTime, Integer, String, func
#String - для пароля,
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

PG_USER = os.getenv("PG_USER", "user")
PG_PASSWORD = os.getenv("PG_PASSWORD", "1234")
PG_DB = os.getenv("PG_DB", "netology")
PG_HOST = os.getenv("PG_HOST", "127.0.0.1")
PG_PORT = os.getenv("PG_PORT", "5431")

PG_DSN = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

engine = create_async_engine(PG_DSN) #создаем асинхронный движок
#базовый класс для асинхронных сессий
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
#Базовый класс для нашей модельки
Base = declarative_base()


class User(Base):

    __tablename__ = "app_users" # обзываем таблицу
#зоздаем поля для таблици
    id = Column(Integer, primary_key=True) #цифровая колонка
    #Строковая колонка, уникальное имя, проиндексировано, не может быть пустым
    name = Column(String, unique=True, index=True, nullable=False)
    #пароль - строковая колонка, не уникальная, не проиндексированная, не может быть пустым
    password = Column(String, nullable=False)
    #Время - время на стороне базы данных (func)
    creation_time = Column(DateTime, server_default=func.now())
