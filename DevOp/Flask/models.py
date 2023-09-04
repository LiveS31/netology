import os
from sqlalchemy import create_engine, Column, Integer, DateTime, String, func
#создает подключение к базе
# func - отвечает за выполнения функций на стороне базы
import atexit # будет разрывать соединение с базой после завершиния программы
from sqlalchemy.orm import sessionmaker #Для создания сессий
from sqlalchemy.ext.declarative import declarative_base # базовый класс для создания функций


PG_USER = os.getenv('PG_USER', 'app')
PG_PASSWORD = os.getenv('PG_PASSWORD', '1234')
PG_DB = os.getenv('PG_DB', 'app')
PG_HOST = os.getenv('PG_HOST', '127.0.0.1')
PG_PORT = os.getenv('PG_PORT', 5431)

PG_DSN = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}'
# Указываем базу данных, пользователя, пароль, .....

engine = create_engine(PG_DSN) #  создаем подключение к базе данных
atexit.register(engine.dispose) # закрывает выполнение приложение

Session = sessionmaker(bind=engine) # Создаем базовый класс для сессии
Base = declarative_base(bind=engine) # будет использоваться в момент применения миграции

# создаем таблицу
class User(Base):

    __tablename__ = 'app_users'

    id = Column(Integer, primary_key=True) #
    name = Column(String, nullable=False, unique=True, index=True)
# пользователь, не может быть пустым, с неповторяемым именем, включен в индекс поиска)
    password = Column(String, nullable=False)
    create_time = Column(DateTime, server_default=func.now())
# запись времени, взятие даты с сервера (func- за это отвечает)

Base.metadata.create_all()