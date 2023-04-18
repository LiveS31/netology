import configparser
import sqlalchemy
config = configparser.ConfigParser()
config.read('.pass.ini')
DSN = config['dsn']['DSSN']

import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()
class Users(Base):
    __tablename__ = 'users'
    user_id = sq.Column(sq.Integer, primary_key=True)
    user_age = sq.Column(sq.Integer, unique=False)
    user_gender = sq.Column(sq.VARCHAR(10))
    user_city = sq.Column(sq.VARCHAR(50))

class FavoriteClients(Base):
    __tablename__ = 'favoriteclients'
    client_id = sq.Column(sq.Integer, primary_key=True)
    client_name = sq.Column(sq.VARCHAR(20), unique=True)
    client_surname = sq.Column(sq.VARCHAR(50))
    client_link = sq.Column(sq.TEXT)
    client_photos = sq.Column(sq.TEXT)



class Users_Client(Base):
    __tablename__ = 'users_client'
    user_id = sq.Column(sq.Integer, sq.ForeignKey(Users.user_id),primary_key=True)
    favoriteclient_id = sq.Column(sq.Integer, sq.ForeignKey(FavoriteClients.client_id), primary_key=True)

class Users_Propose(Base):
    __tablename__ = 'users_propose'
    user_id = sq.Column(sq.Integer, sq.ForeignKey(Users.user_id), primary_key=True)
    prop_client_id =sq.Column(sq.Integer, unique=True)

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session.close()
def inse_users(user_id, user_age,user_gender,user_city):

create_tables(engine)
#session.close()