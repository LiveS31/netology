import datetime

from django.core.paginator import Paginator
from django.shortcuts import render #библиотека,
# которая позволяет переработать в валидный HTML text
from django.http import HttpResponse
# Create your views here
'''простые запросы'''
def index(request):
    return HttpResponse('hello from django!!!')

def time(request):
    return HttpResponse(f'Time = {datetime.datetime.now().time()}')

'''Параметры запросов'''
def hello(request):
    name = request.GET.get('name') # ПОЛУЧАЕМ ПАРАМЕТРЫ
    age = request.GET.get('age', 20) # получаем параметры и ставим значение поумолчанию
    print (age) # выводим
    return HttpResponse(f'hello, {name}') #отправляем на ответвет на сайт

def sum(request, op1, op2): # параметры <a>/<b> должны называться обязательно одинаково
    result = op1 + op2 # можно так int(op1) + int(op2)
                          #или так <int:op1>/<int:op2>/
    return HttpResponse(f'Sum = {result}')

'''введение в шаблоны:'''
def index2(request):
    context = {          #простой словарь
        'test': 5,
        'data': [1, 5, 8],
        'val' : 'hello',
    }
    return render(request, 'demo.html', context)
#request -обязательный параметр
#demo.html - название шаблона указываем с путем где он лежит
# context - cтавим последним

#пагинация
CONTENT = [str(i) for i in range (10000)]
# список страниц(от 1 до 10000 - в данном случае)
def pagi(request):
    paginotor = Paginator(CONTENT, 10)
#Paginator - класс его нудно импортировать
#paginator - переменная
#CONTENT - список количества страниц
#10- отображение элементов
    page_number = int(request.GET.get('page', 1))
#int(request.GET('page', 1)) - чтобы страницу мог указать пользователь
#если он не укажет, по умолчанию 1
    page = paginotor.get_page(page_number)
# paginotor.get_page(5) - 5 что страница,для отображения
    context ={
        'page':page
    }
#page - положим в контекст
    return render(request, 'pagi.html', context)