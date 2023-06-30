from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet #импортируем

from .models import Adv
from .permissions import IsOwnerOrReadOnly
from .serializers import AdvSerializer


class AdvViewSet(ModelViewSet):#наследуем от ModelViewSet
    queryset = Adv.objects.all() #берет данные их модели AVD
    serializer_class = AdvSerializer #описываем serialiser_class
    permission_classes = [IsOwnerOrReadOnly] #задаем значение,
    # что удалить может только тот кто написао объявления

# включаем фильтрацию для анонимных пользователей
    throttle_classes = [AnonRateThrottle]

#переопределям методы создания объекта
    def perform_create(self, serializer):# есть разные функции для разных действий
    #в данном примере вызываем сохранение данных в базу по аутофикации пользователя
    #делаем в нем запрос корректного юзера
    #user=self.request.user
        serializer.save(user=self.request.user)
