import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User_Favorit(Base):
    __tablename__ = "user_favorite"
    id_user_favorit = sq.Column(sq.Integer, primary_key=True)
    favorit = sq.Column(sq.String, unique=True)

class User_photo(Base):
    __tablename__ = "user_photo"
    id_user_photo = sq.Column(sq.Integer, primary_key=True)
    user_photo = sq.Column(sq.String, unique=True)

class User(Base):
    __tablename__ = "user"
    id_user = sq.Column(sq.Integer, primary_key=True)
    first_name = sq.Column(sq.String)
    last_name = sq.Column(sq.String)
    gender = sq.Column(sq.String)
    age = sq.Column(sq.Integer)
    city = sq.Column(sq.String)
    user_side = sq.Column(sq.String, unique=True)


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
