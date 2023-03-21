# *args - кортеж позиционных аргументов - значение
# все аргумены попадут в args
# **kwargs - Словарь именных аргументов - аргуметты
# def foo(*args, **kwargs):
     #print (args) - передаются ('arg_1', 'arg_2')
     #print (kwargs) - передаются {'named_1':'1', 'named_2':'2'}
#       как словарь
    # return

# функция в пайтоне это аргумент
# ее можно передать,
# сделать ее принть (не вызывая ее)
# передаь в другую функцию, в словари....
# вызвать функцию -> другой фунцией
#декоратор (я думаю и функцию) можно вызывать:
# @print_decor
# def summator(a,b):
#   return                  - аналогично: summator = print_decor(summator)
#####
# пример
#####
def trace(old_function):
    def new_function(*args, **kwargs):
    # до выполнения функции действия
        print(f'Вызвана функция {old_function.__name__} с аргументами {args} и {kwargs}')
# где __name__ - имя функции (вывод словом не значением в ячейке)
        result = old_function(*args, **kwargs)
        print(f'Возвращено: {result}')

        return result
    new_function.__name__ = old_function.__name__
    # если мы хотим сохранить имя функции
    return new_function
@trace #- вызов декоратора
def multiply(a,b): # - функция, которая будет в декораторе
    return a*b
#multiply (2,4)
from tools import cached
import datetime
import requests
from functools import wraps #- декратор возвращающий функции свое название (то что было до присваивания)
@cached(max_size=100)
# каждую функцию нужно очищать, чтобы не переполнялся cache
# можно написать все это в декораторе, а можно в самой функции
def get_people(people_id):
    return requests.get(f'https://swapi.dev/api/people/{people_id}').json()
# start = datetime.datetime.now()
# print (get_people(1))
# end = datetime.datetime.now()
# print(end - start)
#
start = datetime.datetime.now()
print (get_people(1))
end = datetime.datetime.now()
print(end - start)

print(get_people.__name__) # - узнать вернувю функцию
print(help(get_people))

#@classmethod - узнатьь что это
#@staticmetod
#@
# с лекции
def cached(old_function):
    cache = {}

    def new_function(*args, **kwargs):
        key = f'{args}_{kwargs}'

        if key in cache:
            return cache[key]
        result = old_function(*args, **kwargs)
        cache[key] = result
        return result

    return new_function


import requests
import datetime

from tools import cached


@cached
def get_people(people_id):
    return requests.get(f'https://swapi.dev/api/people/{people_id}').json()


start = datetime.datetime.now()
print(get_people(1))
end = datetime.datetime.now()
print(end - start)

start = datetime.datetime.now()
print(get_people(1))
end = datetime.datetime.now()
print(end - start)
Табельский
Кирилл — 13.03
.2023
20: 31
import requests
import datetime

from tools import cached


# @cached(max_size=50)
class People:

    def __init__(self, people_id, refresh=True):
        self.people_id = people_id
        if refresh:
            self.refresh()

    def refresh(self):
        self.data = requests.get(f'https://swapi.dev/api/people/{self.people_id}').json()

    @property
    def name(self):
        return self.data['name']

    @staticmethod
    def say_hi():
        print('HI')

    @classmethod
    def from_json(cls, json_data):
        people = cls(1, refresh=False)
        people.data = json_data
        return people


people = People.from_json({'name': 'Чубака'})
print(people.name)

people = People(1)
people.say_hi()
print(people.name)

people.refresh()
from functools import wraps


def cached(max_size):
    number_of_calls_with_this_size = 0

    def _cached(old_function):

        cache = {}
        number_of_calls = 0

        @wraps(old_function)
        def new_function(*args, **kwargs):
            key = f'{args}_{kwargs}'
            nonlocal number_of_calls, number_of_calls_with_this_size
            number_of_calls_with_this_size += 1

            number_of_calls += 1
            if key in cache:
                return cache[key]

            if len(cache) >= max_size:
                cache.popitem()

            result = old_function(*args, **kwargs)
            cache[key] = result
            return result

        return new_function

    return _cached


hdef cached(old_function):

    cache = {}

    def new_function(*args, **kwargs):
        key = f'{args}_{kwargs}'

        if key in cache:
            return cache[key]
        result = old_function(*args, **kwargs)
        cache[key] = result
        return result

    return new_function
import requests
import datetime

from tools import cached


@cached
def get_people(people_id):

    return requests.get(f'https://swapi.dev/api/people/{people_id}').json()

start = datetime.datetime.now()
print(get_people(1))
end = datetime.datetime.now()
print(end - start)

start = datetime.datetime.now()
print(get_people(1))
end = datetime.datetime.now()
print(end - start)
Табельский Кирилл — 13.03.2023 20:31
import requests
import datetime

from tools import cached


# @cached(max_size=50)
class People:

    def __init__(self, people_id, refresh=True):
        self.people_id = people_id
        if refresh:
            self.refresh()

    def refresh(self):
        self.data = requests.get(f'https://swapi.dev/api/people/{self.people_id}').json()

    @property
    def name(self):
        return self.data['name']

    @staticmethod
    def say_hi():
        print('HI')

    @classmethod
    def from_json(cls, json_data):
        people = cls(1, refresh=False)
        people.data = json_data
        return people


people = People.from_json({'name': 'Чубака'})
print(people.name)

people = People(1)
people.say_hi()
print(people.name)

people.refresh()
from functools import wraps


def cached(max_size):

    number_of_calls_with_this_size = 0

    def _cached(old_function):

        cache = {}
        number_of_calls = 0

        @wraps(old_function)
        def new_function(*args, **kwargs):
            key = f'{args}_{kwargs}'
            nonlocal number_of_calls, number_of_calls_with_this_size
            number_of_calls_with_this_size += 1

            number_of_calls += 1
            if key in cache:
                return cache[key]

            if len(cache) >= max_size:
                cache.popitem()

            result = old_function(*args, **kwargs)
            cache[key] = result
            return result

        return new_function
    return _cached
#https://github.com/tabelsky/decorator_netologyttps: // github.com / tabelsky / decorator_netology
