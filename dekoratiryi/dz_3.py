import os
from datetime import datetime


# Доработать декоратор logger в коде ниже.
# Должен получиться декоратор, который записывает в файл 'main.log' дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась, и возвращаемое значение. Функция test_1
# в коде ниже также должна отработать без ошибок.


def logger(old_function):
    new_functions = old_function
    #print(new_functions)
    def new_function(*args, **kwargs):

        #print(args, kwargs)
        date_time = datetime.now()
        func_name = old_function.__name__
        result = new_functions(*args, **kwargs)
        with open('main.log', 'a', encoding= 'utf-8') as f:
            f.write(f'Дата/время: {date_time}\n'
                    f'Имя функции: {func_name}\n'
                    f'Аргумент {args} - {kwargs}\n'
                    f'Результат {result}\n')
            return result
    return new_function




def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()

#2.Доработать параметризованный декоратор logger в коде ниже. Должен получиться декоратор,
# который записывает в файл дату и время вызова функции, имя функции,
# аргументы, с которыми вызвалась, и возвращаемое значение.
# Путь к файлу должен передаваться в аргументах декоратора.
# Функция test_2 в коде ниже также должна отработать без ошибок.
#import os


def logger(path):

    file = path

    def __logger(old_function):
        def new_function(*args, **kwargs):
            date_time = datetime.now()
            func_name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open(f'{file}', 'a', encoding= 'utf-8') as f:
                f.write(f'Дата/время: {date_time}\n'
                            f'Имя функции: {func_name}\n'
                            f'Аргумент {args} - {kwargs}\n'
                            f'Результат {result}\n')
                return result

        return new_function
    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()

#  Применить написанный логгер к приложению из любого предыдущего д/з.


def logger(old_function):
    new_functions = old_function
    print(new_functions.__name__)
    def new_function(*args, **kwargs):

        print(args, kwargs)
        date_time = datetime.now()
        func_name = old_function.__name__
        result = new_functions(*args, **kwargs)
        with open('maining.log', 'a', encoding= 'utf-8') as f:
            f.write(f'Дата/время: {date_time}\n'
                    f'Имя функции: {func_name}\n'
                    f'Аргумент {args} - {kwargs}\n'
                    f'Результат {result}\n')
            return result
    return new_function
def test_3():
    @logger
    def para(boys, girls):
        a = []
        boys.sort(), girls.sort()
        if len(boys) != len(girls):
            f = 'Kто-то может остаться без пары!'
            print('Kто-то может остаться без пары!')
        else:
            for i in range(len(boys)):
                f = f'{boys[i]} и {girls[i]}'
                a.append(f)
                print(f'{boys[i]} и {girls[i]}')
        return a
    para (['Peter', 'Alex', 'John', 'Arthur', 'Richard'],['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'])
#чуть изменил для большей инфы

if __name__ in '__main__':
    test_3()
