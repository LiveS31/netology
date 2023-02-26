import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import configparser
config = configparser.ConfigParser()
config.read('1.ini')
code_dsn = config['dsn']['DSSN']

from models import create_tables, Publisher, Shop, Book, Stock, Sale # импортируем классы из файла models
# + функцию создания таблиц

DSN = code_dsn # из другого файла
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()


def insert_table():# функция заполнения таблиц из файла 'tests_data.json'

    with open('tests_data.json', 'r') as fd:# считываем файл
        data = json.load(fd)

    for record in data:# заполняем таблицы
        model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()


#поиск по таблицам
def filter_publisher(name_publisher):#
    if name_publisher.isnumeric():
        return name_publisher

    else:
        id_publisher = session.query(Publisher.id).filter(Publisher.name == name_publisher).scalar()
        return id_publisher

def selection_publisher(id_publisher):#
    for result in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Sale.stock). \
            join(Stock.shop).join(Stock.book).filter(Book.id_publisher == id_publisher).all():
        print_list = list(result)
        print(f'{print_list[0]}|\t'
              f'{print_list[1]}|\t'
              f'{int(print_list[2])}|\t'
              f'{print_list[3].strftime("%d-%m-%Y")}')
    session.commit()

if __name__ == '__main__':# начало кода
    create_tables(engine)
    insert_table()
    selection_publisher(filter_publisher(input('Введите имя или номера в таблице publisher: ')))
    session.close()
