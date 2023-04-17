import sqlalchemy
from sqlalchemy import *
from sqlalchemy import MetaData
import configparser
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, sessionmaker
config =configparser.ConfigParser()
config.read('.pass.ini')
#Base = declarative_base()
#DNS = config['dsn']['DSSN']
#from sqlalchemy.orm import declarative_base, Session



Base = declarative_base()
engine = sqlalchemy.create_engine(config['dsn']['DSSN'])
Session = sessionmaker(bind=engine)
session = Session()
class Users(Base):
    __tablename__ = 'users'
    user_id = sq.Column(sq.Integer, primary_key=True)
    user_age = sq.Column(sq.Integer)
    user_gender = sq.Column(sq.VARCHAR(10))
    user_city = sq.Column(sq.VARCHAR(50))

class FavoriteClients(Base):
    __tablename__ = 'favoriteclients'
    client_id = sq.Column(sq.Integer, primary_key=True)
    client_name = sq.Column(sq.VARCHAR(20))
    client_surname = sq.Column(sq.VARCHAR(50))
    client_link = sq.Column(sq.TEXT)
    client_photos = sq.Column(sq.TEXT)



class Users_Client(Base):
    __tablename__ = 'users_client'
    user_id = sq.Column(sq.Integer, sq.ForeignKey(Users.user_id),primary_key=True)
    favoriteclient_id = sq.Column(sq.Integer, sq.ForeignKey(FavoriteClients.client_id))

class Users_Propose(Base):
    __tablename__ = 'users_propose'
    user_id = sq.Column(sq.Integer, sq.ForeignKey(Users.user_id), primary_key=True)
    prop_client_id =sq.Column(sq.Integer)

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session.close()
create_tables(engine)

#
# class Users(Base):
#     __table__ = Table('users', metadata, autoload=True)
#
#
# class User_Client(Base):
#     __table__ = Table('users_client', metadata, autoload=True)
#
#
# class Favorite(Base):
#     __table__ = Table('favorite', metadata, autoload=True)
#
#
# class Users_Propose(Base):
#     __table__ = Table('users_propose', metadata, autoload=True)
#
#
# users = Users
# user_client = User_Client
# user_prop = Users_Propose
# favorite = Favorite


def ins_data(user_id, user_age, user_gender, user_city):
    conn = engine.connect()
    sel = select(Users).where(Users.user_id == user_id)
    if conn.execute(sel).fetchall():
        upd = update(Users).where(Users.user_id == user_id).values(
            user_age=user_age,
            user_gender=user_gender,
            user_city=user_city
        )
        conn.execute(upd)
    else:
        ins = insert(Users).values(
            user_id=user_id,
            user_age=user_age,
            user_gender=user_gender,
            user_city=user_city
        )
        conn.execute(ins)


def ins_fav_data(user_id, client_id, client_name, client_surname, client_link, client_photo):
    conn = engine.connect()
    sel = select(FavoriteClients).where(FavoriteClients.client_id == client_id)
    if conn.execute(sel).fetchall():
        return
    else:
        ins = insert(FavoriteClients).values(
            client_id=client_id,
            client_name=client_name,
            client_surname=client_surname,
            client_link=client_link,
            client_photos=client_photo
        )
        conn.execute(ins)
        ins_user_client(user_id, client_id)
        print('add to favorite')


def ins_user_client(user_id, fav_client_id):
    conn = engine.connect()
    ins = insert(Users_Client).values(
        user_id=user_id,
        favoriteclient_id=fav_client_id
    )
    conn.execute(ins)


def ins_propose_data(user_id, client_id):
    conn = engine.connect()
    sel = select(Users_Propose).where(and_(Users_Propose.prop_client_id == client_id, Users_Propose.user_id == user_id))
    if conn.execute(sel).fetchall():
        return
    else:
        ins = insert(Users_Propose).values(
            user_id=user_id,
            prop_client_id=client_id
        )
        conn.execute(ins)
        print('add to user_prop')


def sel_prop_data(user_id):
    conn = engine.connect()
    sel = select(Users_Propose).where(Users_Propose.user_id == user_id)
    res = conn.execute(sel)
    res_list = [i for i in res]
    return res_list


# Выбор запроса по пользователю
def sel_user_data(user_id):
    conn = engine.connect()
    sel = select(Users).where(Users.user_id == user_id)
    res = conn.execute(sel)
    res_list = ([i for i in res])
    return res_list


def select_fav_client(user_id):
    conn = engine.connect()
    sel = select(FavoriteClients).join(Users_Client).where(Users_Client.user_id == user_id)
    res = conn.execute(sel)
    res_list_fav = ([i for i in res])
    return res_list_fav

#create_tables(engine)
ins_fav_data(1, '2', 'dggdg', 'gddgd', 'dfgd', 'dgdfgdgd')
ins_data(1, 33, 'dgd', 'dfwgd')
session.close()