import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
class Photo(Base):
    __tablename__ = "photo"
    photo_id = sq.Column(sq.Integer, primary_key=True)
    vk_offer_id =sq.Column(sq.Integer, unique=True)
    photo_url = sq.Column(sq.String)

class Offer(Base):
    __tablename__ = 'offer'
    vk_offer_id = sq.Column(sq.Integer, primary_key=True)
    first_name = sq.Column(sq.String)
    last_name = sq.Column(sq.String)
    sex = sq.Column(sq.String)
    age = sq.Column(sq.String)
    city = sq.Column(sq.String)

class User_offer_id(Base):
    __tablename__ = 'user_offer_id'
    user_offer_id = sq.Column(sq.Integer, primary_key=True)
    vk_user_id = sq.Column(sq.Integer, unique=True)
    black_list = sq.Column(sq.String)
    favorite_list = sq.Column(sq.String)

class User(Base):
    __tablename__ = 'user'
    vk_user_id = sq.Column(sq.Integer, primary_key=True)
    first_name = sq.Column(sq.String)
    sex = sq.Column(sq.String)
    age = sq.Column(sq.String)
    city = sq.Column(sq.String)

class Interest_person(Base):
    __tablename__ = 'interest_person'
    interest_person_id = sq.Column(sq.Integer, primary_key=True)
    interest_id = sq.Column(sq.Integer, unique=True)
    vk_user_id = sq.Column(sq.Integer, unique=True)
    vk_offer_id = sq.Column(sq.Integer, unique=True)

class Interest(Base):
    __tablename__ = 'interest'
    interest_id = sq.Column(sq.Integer, primary_key=True)
    interest = sq.Column(sq.String)


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

