from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
# Create your views here.
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


# создадим класс ViewSet
# class CommentViewSet(ViewSet):
#     def list(self, request): # позволяем вывести все объекты данноо ресурса
#         return Response({'status':'Ok'})
#
#     #если хотим смотреть какой-то конкретный объект
#     def retrieve(self, request):
#         pass
#
#     #для удаления обекта
#     def destroy(self, request):
#         pass
#     # для обновления
#     def update(self, request):
#         pass
#     # для создания
#     def create(self, request):
#         pass
#

#но можно проще. в методе ModelViewSet - все вышеперечисленные методы реализованы

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all() # откуда берем данные
    serializer_class = CommentSerializer
    #создаем файл serializers
    #чтобы настроить фильтрацию
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user', ]
    search_fields = ['text',]   #поиск по полям текст
    # (можем делать поиск по коментариям в поле текст)
# как искать
#GET http://localhost:8000/omments/?seach=text
    #третий тип фильтра - отвечает за упорядовачивание
    ordering_fieds = ['id', 'user', 'text', 'created_at'] #вводим список
# параметров которые необходимо порядочить. в данномсписке рперечисляются те поля
# по которым можно фильравать
# чтобы сделать запрос
#GET http://localhost:8000/omments/?q=text&ordering=id
# это значит упорядочить по id/ (если нужно в обратном порядке -id)
# если нужно по вум параметрам id, text
    pagination_class = LimitOffsetPagination
    # сколько показать, сколько пропустить