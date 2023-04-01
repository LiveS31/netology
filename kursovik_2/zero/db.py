import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import create_tables
from settings import postgresql

system = 'postgresql'
login = 'postgres'
password = postgresql
host = 'localhost'
port = 5432
name_db = 'vkinder_db_zero'
DSN = f'{system}://{login}:{password}@{host}:{port}/{name_db}'
engine = sq.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()
create_tables(engine)


def add_user_profile(list_):
    pass


# есть ли анкета
def favorite_profile_bd(id_):
    pass


def add_photo(id_):
    pass


if __name__ == '__main__':
    session.close()
