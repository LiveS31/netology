from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response


from .models import Wearpon #импортируем модель

from .serialisers import WeaponSerializer # импортируем полученный конвектатор
from rest_framework.views import APIView
#@api_view(['GET']) #декоратор из библиотеки
# def game(request):
#     weapons = Wearpon.objects.all() # делаеgameм запрос в базу данных
#     ser = WeaponSerializer(weapons, many=True) #Заводим его в переменную.
#                                             # и говорим, что данных много
#     data = {'message':'Hello'} #словарь сообщение и текст сообения
#     #return Response(data) # Response - обработчик импортируем
#     return Response(ser.data) #выводим новый результат данных
#     #с учетом введенных данных в таблицу

#теперь реализуем с поддержкой двух запросов

#@api_view(['GET', 'POST'])
# def game(request):
#     if request.method == 'GET':
#         weapons = Wearpon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         return Response(ser.data)
#     if request.method == 'POST':
#         return Response({'status':'Ok'})

#следующий класс будет повторять все действия выше,
# но будет проще с меньшим колличеством кода

# class GameView(APIView): # наследуется от APIView - нужно импортироать
#     def get(self, requst): #метод get, который примнимает request
#         weapons = Wearpon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         return Response(ser.data)
#     def post(self, request): # метод post
#         return Response({'status': 'Ok'})
#    path('demo/', GameView.as_view()), - нужно зарегистрировать
# и импоритировать данный класс

# Следующий метод который может все тоже

class GameView(ListAPIView): #наследуется от ListAPIView
    # нужно импортировать
    queryset = Wearpon.objects.all() # для него требуется указать откуда брать данные
    # с помощью чего превратить полученное в json
    serializer_class = WeaponSerializer
    #данный метод не возвращает POST
    #пожтиму его можно реализовыать через функцию
    def post(self, request):
        return Response({'status':'Ok'})

# для отображения оружия
class WeaponView(RetrieveAPIView): # наследем и нужно его импортировать
    queryset = Wearpon.objects.all()  # для него требуется указать откуда
    serializer_class = WeaponSerializer #Через что отображать
