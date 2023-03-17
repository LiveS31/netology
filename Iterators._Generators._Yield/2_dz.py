class FlatIterator: # создан класс у которого по классике три метода

    def __init__(self, list_of_list):
        self.start = list_of_list # Задаем переменную класса (свойство экземпляра класса
        # ее видимости в других экземплярах)


    def __iter__(self): # экземпляр выполняеся один раз на вход в цикл
        # должен вернуть один объект ( в данном случае next)
        self.list_counter = - 1   #задаем счетчики (свойство )
        self.element_counter = 0
        return self # возвращаем self

    def __next__(self): # выполняется каждый раз при итерации
        if self.list_counter == len(self.start):# условия выхода из итерации
            raise StopIteration # возвращаем по условию (в данном случае при когда счетчик равен длинне
        # raise - выполнить при определенном условии имеющимся в python. (указывается после него )
        item = self.start[self.list_counter][self.element_counter]
        #выполняем действия словаря (приравниваем
        if self.element_counter != len(self.start[self.list_counter]):# условие счетчика
            self.element_counter += 1
        else:# условие счетчика
            self.element_counter = 0
            self.list_counter += 1

        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == 'main':
    test_1()

### 2
import types
def flat_generator(list_of_lists):

    for item_list in list_of_lists:
        for item in item_list:
            yield item # если бы был ретерн- функция бы выполнилась 1раз


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == 'main':
     test_2()