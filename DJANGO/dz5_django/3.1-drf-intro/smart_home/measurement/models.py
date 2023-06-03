from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

#Создаем таблицу Sensor
class Sensor(models.Model):
    name = models.CharField(max_length=50,verbose_name='Название') #Название Sensor
    description = models.CharField(max_length=50, verbose_name='Описание') #Описание#

    #описание в админке
    class Meta:
        verbose_name = 'Сенсор'
        verbose_name_plural = 'Сенсоры'

    #чтобы нормально отображалось
    def __str__(self):
        return self.name
#Создаем таблицу Measurements
class Measurement(models.Model):
    # Создаем связь sensor_id (в таблиице Sensor) с id  в таблице Measurements c каскадным удаление
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Температура') #цифру с десятыми
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время') #дата с реальным обновлением


# данные для админки
    class Meta:
        verbose_name = 'Показание' #дополнительная инфа
        verbose_name = 'Показания'


