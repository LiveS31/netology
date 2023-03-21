# создаем декорирование кеширования
#MAX_SIZE = 1000 # максимальная длинна для очистки cached
from functools import wraps #- декратор возвращающий функции свое название (то что было до присваивания)


def cached(max_size): #называеся фабрика декораторов
    def _cached(old_function):
        cache = {} #создает словарь
        @wraps(old_function) #- применение декоратора для функции
        def new_function(*args, **kwargs): #создам функцию
            key = f'{args}_{kwargs}' # делаем словарь
            if key in cache: #условия
                return cache[key]

            if len(cache) >= max_size: #очистка словаря, чтобы не переполнялся
                cache.popitem()

            result = old_function(*args, **kwargs) #Переменные приравнивание
            cache[key] = result
            return result
        return new_function
    return _cached
cached_20 = cached(20)
#или @caced(max_saze = 20)
def foo():# вызов функции
    pass

