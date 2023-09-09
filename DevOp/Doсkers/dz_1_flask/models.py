import os
import atexit # разрывает соединение с базой после завершения программы
import uuid

from sqlalchemy import create_engine, Column, Integer, DateTime, String, func, ForeignKey
#создает подключение к базе
from sqlalchemy.ext.declarative import declarative_base # базовый класс для создания функций
from sqlalchemy.orm import sessionmaker, relationship  # Для создания сессий
from sqlalchemy_utils import EmailType, UUIDType
#UUIDType - генератор

#принимаем параметры для базы данных

PG_USER = os.getenv('PG_USER', 'user')
PG_PASSWORD = os.getenv('PG_PASSWORD', '1234')
PG_DB = os.getenv('PG_DB', 'app')
PG_HOST = os.getenv('PG_HOST', '127.0.0.1')
PG_PORT = os.getenv('PG_PORT', 5431)

#присваеваем базу данных, пароль,...
PG_DNS = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}'

#подключаемся к базе данных
engine = create_engine(PG_DNS)
#закрываем выполнение приложения
atexit.register(engine.dispose)

#Создается базовай класс для сессии
Session = sessionmaker(bind=engine)
#будет использоваться при миграции
Base = declarative_base(bind=engine)

#создаем таблицы и связи
class User(Base):

    __tablename__ = 'app_users' #имя таблици
    id = Column(Integer, primary_key=True)  # id
    name = Column(String, nullable=False, unique=True, index=True)
    # пользователь, не может быть пустым, с неповторяемым именем, включен в индекс поиска
    password = Column(String, nullable=False)
    #для пароля
    email = Column(EmailType, unique=True, index=True)
    #строчка для записи почты

class Token(Base):

    __tablename__ = 'tokens' #имя таблици
    id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
    # уникальная генерация 4
    create_time = Column(DateTime, server_default=func.now())
    # запись времени, взятие даты с сервера (func- за это отвечает)
    user_id = Column(Integer, ForeignKey('app_users.id', ondelete='CASCADE'))
#создаем связь 'user_id' с таблицей 'app_users.id' и каскадным удалением
    user = relationship('User', lazy='joined')
    #выборка left join (загружать отношения в том же запросе,
    # что и родительский, с помощью оператора JOIN)

class Announcement(Base):

    __tablename__ = 'announcement'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False) #название обявление, при отсутствии создать столбец как NOT NULL
    description = Column(String, nullable=False) # отбъявлениб при отсутствии создать столбец как NOT NULL
    owner = Column(ForeignKey('app_users.id', ondelete='CASCADE'))
#создаем связь 'owner' с таблицей 'app_users.id' и каскадным удалением
    #create_time = Column(DateTime, default=func.now()) #убрать
#(записываем, создаем таблици


Base.metadata.create_all()

