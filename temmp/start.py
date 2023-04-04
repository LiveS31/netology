import configparser

import sqlalchemy
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read('1.ini')
code_dsn = config['dsn']['DSSN']

from table import create_tables  #Publisher, Shop, Book, Stock, Sale # импортируем классы из файла models
# + функцию создания таблиц

DSN = code_dsn # из другого файла
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)
session.close()
