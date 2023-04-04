import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import configparser
from models import create_tables

config = configparser.ConfigParser()
config.read('.pass.ini')
code_dsn = config['dsn']['DSSN']
DSN = code_dsn

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
