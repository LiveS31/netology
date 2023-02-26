import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()
# значение колонок играют роль. хотя не ясно почему
# но с созданием таблиц все относительно понятно
# Создаем классы (каждый класс это таблица
class Publisher(Base):
    __tablename__ = "publisher"
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True)

    def __str__(self):# вывод информации на экран
        return f'Publisher id={self.id}: name={self.name}'

class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title =sq.Column(sq.String, unique=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
    publisher = relationship('Publisher', backref='book')# почитать
    def __str__(self):
        return f'Book id={self.id}: (title={self.title}, id_publisher={self.id_publisher})'

class Shop(Base):
    __tablename__= 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=False)

    def __str__(self):
        return f'Shop id={self.id}: name={self.name}'

class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    shop = relationship('Shop', backref='stock1')# нужно про это почитать
    book = relationship('Book', backref='stock2')

    def __str__(self):
        return f'Stock id={self.id}: (id_book={self.id_book},' \
               f' id_shop={self.id_shop}, count={self.count})'
class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price =  sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.Date,nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer)
    stock = relationship('Stock', backref='sale')
    def __str__(self):
        return f'Sale id={self.id}: (price={self.price}, date_sale={self.date_sale},' \
               f' id_stock={self.id_stock}, count={self.count})'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

