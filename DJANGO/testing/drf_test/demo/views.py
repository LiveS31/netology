from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
#напишем для отобразения и возможности создания
from .models import Message
from .serializers import MessageSerializer


class MessageViewSet(ModelViewSet):
    #получаем данные от родительского класса
    queryset = Message.objects.all()
    #Создаем проверку вводных данных
    serializer_class = MessageSerializer
