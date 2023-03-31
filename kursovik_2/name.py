import configparser
import requests
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from nameAA import create_tables
config = configparser.ConfigParser()
config.read('pass.ini')
code_dsn = config['dsn']['DSSN']

DSN = code_dsn # из другого файла
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    create_tables(engine)
    session.close()
