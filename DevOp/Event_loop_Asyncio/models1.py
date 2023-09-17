import os
#подключение к баз данных
#1. устанавливаем алхимию
#SQLAlchemy==1.4.48
#2. устанавливаем асинхронный драйвед для базы
#asyncpg
from sqlalchemy import JSON, Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# расширение для синхронной работы
from sqlalchemy.ext.declarative import declarative_base
# функция возвращает базовый класс
from sqlalchemy.orm import sessionmaker # базовая сессия  +AsyncSession

PG_USER = os.getenv("PG_USER", "user") #user  - поумолчанию
PG_PASSWORD = os.getenv("PG_PASSWORD", "1234") # пароль
PG_DB = os.getenv("PG_DB", "netology") # база данных
PG_HOST = os.getenv("PG_HOST", "127.0.0.1") # хост
PG_PORT = os.getenv("PG_PORT", "5431") # port

PG_DSN = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
# собираем запрос, но чтобы использовать синхронный запрос postgresql+asyncpg

engine = create_async_engine(PG_DSN) #движок синхронный для работы с таблицами
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
#забираем подключение из движка который был создан, в качестве класса использовать - AsyncSession
#выбираем закрывать сессию по умолчанию или оставить открытой

Base = declarative_base() # базовый класс


class SwapiPeople(Base):
    __tablename__ = "swapi_people" # название таблици
    id = Column(Integer, primary_key=True)
    json = Column(JSON) # строка json в таблице