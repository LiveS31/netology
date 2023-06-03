from rest_framework import serializers
from .models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы

class MeasurementSerializer(serializers.ModelSerializer):
    # создаем класс настледующийся
    class Meta:
        model = Measurement #от какой модели наследуем класс
        fields =['temperature', 'created_at'] #список свойсь для отображения

class MeasuremetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class SensorDetailSerializer(serializers.ModelSerializer):
    #Действия которые можно
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
