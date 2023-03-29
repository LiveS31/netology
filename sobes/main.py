
class Stack:
    def __init__(self):
         self.stack= []
        #"""is_empty — проверка стека на пустоту. Метод возвращает True или False"""
    def is_empty(self):
        return len(self.stack) == False

      #  """push — добавляет новый элемент на вершину стека. Метод ничего не возвращает"""
    def push(self, obj):
        self.stack.append(obj)


        #pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        return self.stack.pop()

       #peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется
    def peek(self):
        return self.stack[-1]


        #size — возвращает количество элементов в стеке
    def size(self):
        return len(self.stack)