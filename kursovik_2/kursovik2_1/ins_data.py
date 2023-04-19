import sqlalchemy
from sqlalchemy import *
import configparser
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, sessionmaker
config = configparser.ConfigParser()
config.read('.pass.ini')

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
    user_id = sq.Column(sq.Integer)
    client_name = sq.Column(sq.VARCHAR(20))
    client_surname = sq.Column(sq.VARCHAR(50))
    client_link = sq.Column(sq.TEXT)
    client_photos_1 = sq.Column(sq.TEXT)
    client_photos_2 = sq.Column(sq.TEXT)
    client_photos_3 = sq.Column(sq.TEXT)



class Users_Client(Base):
    __tablename__ = 'users_client'
    user_id = sq.Column(sq.Integer, sq.ForeignKey(Users.user_id), primary_key=True)
    favoriteclient_id = sq.Column(sq.Integer, sq.ForeignKey(FavoriteClients.client_id), primary_key=True)


class Users_Propose(Base):
    __tablename__ = 'users_propose'
    user_id = sq.Column(sq.Integer, sq.ForeignKey(Users.user_id), primary_key=True)
    prop_client_id = sq.Column(sq.Integer, primary_key=True)

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session.close()
#create_tables(engine)
    print ('111111111----')

def ins_data(user_id, user_age, user_gender, user_city):#

    if (session.query(Users).filter(Users.user_id == user_id).first() is None):
        session.add(Users
                (
                user_id=user_id,
                user_age=user_age,
                user_gender=user_gender,
                user_city=user_city
                )
            )
    else:
        user= session.query(Users).filter(Users.user_id== user_id).first()
        user.user_id= user_id
        user.user_age= user_age
        user.user_gender= user_gender
        user.user_city =user_city
    session.commit()


def ins_fav_data(user_id, client_id, client_name, client_surname, client_link, client_photo):#
    if 3 - len(client_photo) != 0:
        for i in range(3-len(client_photo)):
            client_photo.append('ОТСУТСТВУЕТ')

    print((client_photo))
    if (session.query(FavoriteClients).filter(FavoriteClients.client_id == client_id).first() is None):
        session.add(FavoriteClients
            (

            client_id=client_id,
            user_id=user_id,
            client_name=client_name,
            client_surname=client_surname,
            client_link=client_link,
            client_photos_1=client_photo[0],
            client_photos_2=client_photo[1],
            client_photos_3=client_photo[2]

        )
        )
    else:
        user = session.query(FavoriteClients).filter(FavoriteClients.client_id == client_id).first()

        user.client_id = client_id,
        user.user_id = user_id,
        user.client_name = client_name,
        user.client_surname = client_surname,
        user.client_link = client_link,
        user.client_photos_1 = client_photo[0],
        user.client_photos_2 = client_photo[1],
        user.client_photos_3 = client_photo[2]
    session.commit()
    print('add to favorite')


def ins_user_client(user_id, fav_client_id):#
    if (session.query(Users_Client).filter(Users_Client.user_id == user_id).first() is None):
        session.add(Users_Client
                (
                user_id=user_id,
                favoriteclient_id=fav_client_id,
                )
            )
    else:
        user= session.query(Users_Client).filter(Users_Client.user_id== user_id).first()
        user.user_id= user_id
        user.favoriteclient_id=fav_client_id
    session.commit()



def ins_propose_data(user_id, client_id):
    if (session.query(Users_Propose).filter(Users_Propose.user_id == user_id).first() is None):
        session.add(Users_Propose
                (
                user_id=user_id,
                prop_client_id=client_id,
                )
            )
    else:
        user= session.query(Users_Propose).filter(Users_Propose.user_id== user_id).first()
        user.user_id= user_id
        user.prop_client_id=client_id
    session.commit()
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
    sel = select(FavoriteClients).where(FavoriteClients.user_id == user_id)
    res = conn.execute(sel)
    res_list_fav = ([i for i in res])
    print (res_list_fav)
    return res_list_fav

#create_tables(engine)
#select_fav_client(769656100)
#b = ['gdgd']#['fsdfs1111','fgdfg' ]
# ins_user_client(1, 1)
#ins_fav_data(1, 2, 'dggdg', 'gddgd', 'dfgd', b)#, 'ewrwe', 'wrwrww')
#ins_data(1, 33, 'dgd', 'djjjd')
# ins_propose_data(1,2)
#session.commit()
#session.close()