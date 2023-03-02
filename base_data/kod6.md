import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
# declarative_base - специальный клас который регистрирует всех своих наследников


class Course(Base):
    __tablename__ = "course"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    # homeworks = relationship("Homework", back_populates="course")
    # def __str__ (self):
        return f'{self.id}:{self.name}'
    #str преобразует вывод кода в обычном виде, а не номером ячейки памяти
    #{self.id}:{self.name},{self....},{self....} - указываем попя таблици, которые нам будут нужны

class Homework(Base):
    __tablename__ = "homework"

    id = sq.Column(sq.Integer, primary_key=True)
    number = sq.Column(sq.Integer, nullable=False)
    description = sq.Column(sq.Text, nullable=False)
    course_id = sq.Column(sq.Integer, sq.ForeignKey("course.id"), nullable=False)

    # course = relationship(Course, back_populates="homeworks")
    #relationship - описывает с какой таблицей мы хотим связаться
    #back_populates - какое обратное свойство будет сязываться с нами

    course = relationship(Course, backref="homeworks")
# backref - альтернативный способ создания связей в таблицах.
# оно автоматически создаст связи

def create_tables(engine):
    # Base.metadata.drop_all(engine) #удаление всех таблиц
    Base.metadata.create_all(engine) #создание страниц


DSN = "postgresql://postgres:postgres@localhost:5432/netology_db" #- формирование запроса (логин, пароль,порт, база данных)
#engine - переменная
engine = sqlalchemy.create_engine(DSN) # - подключение к postgres
create_tables(engine)

# сессия
Session = sessionmaker(bind=engine) #- связь ссессии с нашим движком
# Session - типа создание классса создание ссессии
session = Session()
# session - это подключение к базам данных , аналог курсора
# создается при помощи sessionmaker -from sqlalchemy.orm import sessionmaker
# После работы требуется закрывать

# создание объектов

js = Course(name="JavaScript")
print(js.id)
hw1 = Homework(number=1, description="первое задание", course=js)
hw2 = Homework(number=2, description="второе задание (сложное)", course=js)

session.add(js) # - добовляем изменения
print(js.id)
session.add_all([hw1, hw2])
session.commit()  # фиксируем изменения
print(js.id)


# запросы
session.query(КЛАСС).all() - показать все курсы
Можно пробезаться по всем курсам
for c in session.query(КЛАСС).all():
print (c)
filter - позволяет делать фильтр для выборки. (указыается на таблица , а класс таблици)
for c in session.query(КЛАСС).filter(Homework.number == 1).all():
print (c)

q = session.query(Course).join(Homework.course).filter(Homework.number == 1) -??

for session.query(Course).join(Homework.course).filter(Homework.number == 1).all():
    print(q)
for s in q.all():
    print(s.id, s.name)
    for hw in s.homeworks:
        print("\t", hw.id, hw.number, hw.description)

# вложенный запрос
subquery - это подзапрос
subq = session.query(Homework).filter(Homework.description.like("%сложн%")).subquery("simple_hw")
q = session.query(Course).join(subq, Course.id == subq.c.course_id)
.join(subq, Course.id == subq.c.course_id) - описание по какому (каким) столбцам объединяется таблица
РЕЗУЛЬТАТЫ ХРАНЯТСЯ В ПОЛЕ - "С"
вывод результатов
for c in session.query(Course).join(subq, Course.id == subq.c.course_id).all():
    print(c)
    или так
for s in q.all():
    print(s.id, s.name)
    for hw in s.homeworks:
        print("\t", hw.id, hw.number, hw.description)


# обновление объектов
session.query(Course).filter(Course.name == "JavaScript").update({"name": "NEW JavaScript"})
session.commit()  # фиксируем изменения


# удаление объектов
session.query(Homework).filter(Homework.number > 1).delete()
session.commit()  # фиксируем изменения
