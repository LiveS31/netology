import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
#from settings import postgresql
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from models_db import create_tables, User, FavoritesProfile, Photos, BlackProfile
from vk_info_user import get_photo, sort_photo

system = 'postgresql'
login = 'postgres'
password = 'postgres'
host = 'localhost'
port = 5432
name_db = 'vkinder_db_zero'
DSN = f'{system}://{login}:{password}@{host}:{port}/{name_db}'
engine = sq.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()
create_tables(engine)


def add_user(vk_id):
    """Adds a user to the database."""
    if check_user(vk_id) is None:
        try:
            new_user = User(vk_id=vk_id)
            session.add(new_user)
            session.commit()
            return True
        except(IntegrityError, InvalidRequestError):
            return False
    else:
        pass


def check_user(vk_id):
    """Checks the user in the database. Auxiliary function."""
    current_user_id = session.query(User).filter_by(vk_id=vk_id).first()
    return current_user_id


def add_user_profile(list_, vk_id):
    """Adds questionnaires to the table 'favorites_profile'."""
    if favorite_profile_bd(list_[0]) is None:
        new_profile = FavoritesProfile(vk_id=list_[0], first_name=list_[1], last_name=list_[2], city=list_[4],
                                       link=list_[5], id_user=get_id_user_for_fl(vk_id))
        session.add(new_profile)
        session.commit()
        return True
    else:
        return False


def add_black_user_profile(list_, vk_id):
    """Adds questionnaires to the table 'black_profile'."""
    if black_profile_bd(list_[0]) is None:
        new_profile = BlackProfile(vk_id=list_[0], first_name=list_[1], last_name=list_[2], city=list_[4],
                                   link=list_[5], id_user=get_id_user_for_fl(vk_id))
        session.add(new_profile)
        session.commit()
        return True
    else:
        return False


def favorite_profile_bd(vk_id):
    """Checks the questionnaires in the table 'favorites_profile'."""
    current_user_id = session.query(FavoritesProfile).filter_by(vk_id=vk_id).first()
    return current_user_id


def black_profile_bd(vk_id):
    """Checks the questionnaires in the table 'black_profile'."""
    current_user_id = session.query(BlackProfile).filter_by(vk_id=vk_id).first()
    return current_user_id


def get_id_user_for_fl(vk_id):
    """Gets a foreign key for the tables."""
    db_favorites = session.query(User).filter_by(vk_id=vk_id).all()
    id_fl = ''
    for i in db_favorites:
        id_fl = i.id_user
    return int(id_fl)


def get_id_fp_for_photos(vk_id):
    """Gets a foreign key for the table 'photos'."""
    db_favorites = session.query(FavoritesProfile).filter_by(vk_id=vk_id).all()
    id_fp = ''
    for i in db_favorites:
        id_fp = i.id_favorites_profile
    return int(id_fp)


def check_db_favorites(vk_id):
    """Checks the questionnaires in the table 'favorites_profile'."""
    current_users_id = check_user(vk_id)
    all_users = session.query(FavoritesProfile).filter_by(id_user=current_users_id.id_user).all()
    return all_users


def check_db_black(vk_id):
    """Checks the questionnaires in the table 'black_profile'."""
    current_users_id = check_user(vk_id)
    all_users = session.query(BlackProfile).filter_by(id_user=current_users_id.id_user).all()
    return all_users


def add_photo(vk_id):
    """Adds a photo to the table."""
    list_ = sort_photo(get_photo(vk_id))
    for i in list_:
        new_photo = Photos(count_likes=i[0], link_foto=i[1], id_favorites_profile=get_id_fp_for_photos(vk_id))
        session.add(new_photo)
        session.commit()
    return True
