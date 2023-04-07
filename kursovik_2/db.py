import configparser
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from models import create_tables, User, FavoritesProfile, Photos
from vk_info_user import get_photo, sort_photo


config = configparser.ConfigParser()
config.read('.pass.ini')
code_dsn = config['dsn']['DSSN']
DSN = code_dsn

engine = sq.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()
create_tables(engine)


def add_user(vk_id):
    #  добавляет нового пользователя
    try:
        new_user = User(vk_id=vk_id)
        session.add(new_user)
        session.commit()
        return True
    except(IntegrityError, InvalidRequestError):
        return False


def check_user(id_):
    # проверяет есть ли пользователь
    current_user_id = session.query(User).filter_by(vk_id=id_).first()
    return current_user_id


def add_user_profile(list_):
    if favorite_profile_bd(list_[0]) is None:
        new_profile = FavoritesProfile(vk_id=list_[0], first_name=list_[1], second_name=list_[2], link=list_[3])
        session.add(new_profile)
        session.commit()
        return True
    else:
        return False


# есть ли анкета
def favorite_profile_bd(id_):
    current_user_id = session.query(FavoritesProfile).filter_by(vk_id=id_).first()
    return current_user_id


def add_photo(id_):
    list_ = sort_photo(get_photo(id_))
    for i in list_:
        new_photo = Photos(count_likes=i[0], link_foto=i[1])
        session.add(new_photo)
        session.commit()
    return True


if __name__ == '__main__':
    session.close()