import configparser
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from kursovik_2.kursovik2_1.models import create_tables, User, FavoritesProfile, Photos, Temp
from vk_info_user import get_photo, sort_photo


config = configparser.ConfigParser()
config.read('.pass.ini')
code_dsn = config['dsn']['DSSN']
#code_dsn =config['vk']['KEY_GROUP']
DSN = code_dsn

engine = sq.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()
create_tables(engine)

def check_user(id_):
    # проверяет есть ли пользователь
    current_user_id = session.query(User).filter_by(vk_id=id_).first()
    return current_user_id

def add_user(vk_id, list_=None): # тут на данном этапе неверно ( все будет зависить от передачи - я после заменю
    #  добавляет нового пользователя
    try:
        new_user = User(vk_id=vk_id, first_name=list_[1], second_name=list_[2], sex=list_[3], city=list_[4])
        session.add(new_user)
        session.commit()
        return True
    except(IntegrityError, InvalidRequestError):
        return False

def add_user_profile(list_):
    if favorite_profile_bd(list_[0]) is None:
        new_profile = FavoritesProfile(link=list_[0], id_user=list_[1])
        session.add(new_profile)
        session.commit()
        return True
    else:
        return False


# есть ли анкета
def favorite_profile_bd(id_):
    current_user_id = session.query(FavoritesProfile).filter_by(id_user=id_).first()
    return current_user_id


def add_photo(id_):
    list_ = sort_photo(get_photo(id_))
    for i in list_:
        new_photo = Photos(link_foto=i[0], id_favorites_profile=i[1])
        session.add(new_photo)
        session.commit()
    return True


# добовление словарем во временную таблицу
def add_temp (id_, f_name=None, s_name=None, sex=None, city=None, link_pr=None, link_foto=None, count_likes=None):
    table_temp = Temp (vk_id=id_, first_name=f_name, second_name=s_name, sex=sex, city=city, link_prof=link_pr,
                       link_foto=link_foto, count_likes=count_likes )
    session.add(table_temp)
    session.commit()
    return True

if __name__ == '__main__':
    session.close()