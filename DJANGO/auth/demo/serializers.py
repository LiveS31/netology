from rest_framework import serializers

from .models import Adv


class AdvSerializer(serializers.ModelSerializer):
    #создаем class serializers и наследуем его от serializers
    class Meta: # создаем класс мета
        model = Adv # основываемся на модели Avd
        #перечислим все поля которые нужно отбражать ввиде джейсона
        fields = ['id', 'user', 'text', 'created_at', 'open']
#read_only_fields - значит поле разрешено только для чтения
        read_only_fields = ['user',]