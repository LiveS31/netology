import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import Column, Integer, String
# расширение для синхронной работы
from sqlalchemy.ext.declarative import declarative_base
# функция возвращает базовый класс
from sqlalchemy.orm import sessionmaker # базовая сессия  +AsyncSession

# применяем параметры базы данных типа пользователя
# если нет применяем данные после запятой
PG_USER = os.getenv("PG_USER", "user") #user  - поумолчанию
PG_PASSWORD = os.getenv("PG_PASSWORD", "1234") # пароль
PG_DB = os.getenv("PG_DB", "netology") # база данных
PG_HOST = os.getenv("PG_HOST", "127.0.0.1") # хост
PG_PORT = os.getenv("PG_PORT", "5431") # port


# собираем запрос на достум к созданной БД, но чтобы использовать синхронный запрос postgresql+asyncpg
PG_DSN = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

#движок синхронный для работы с таблицами
engine = create_async_engine(PG_DSN)

#забираем подключение из движка который был создан, в качестве класса использовать - AsyncSession
#выбираем закрывать сессию по умолчанию или оставить открытой
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base() # базовый класс

#создаем таблицу  и наследуем от базового класса
class SwapiInfo(Base):

    __tablename__= 'swapi_info' #название таблици
    #делаем строки таблици согласно заданию
    id = Column(Integer, primary_key=True)
    birth_year = Column(String)
    eye_color = Column(String)
    films = Column(String)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(String)
    homeworld = Column(String)
    mass = Column(String)
    name = Column(String)
    skin_color = Column(String)
    species = Column(String)
    starships = Column(String)
    vehicles =Column(String)
