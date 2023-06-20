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
    permission_classes = [IsOwnerOrReadOnly]
    throttle_classes = [AnonRateThrottle]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
