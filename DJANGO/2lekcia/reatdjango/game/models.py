from django.db import models


#создаем класс оружия для наглядности
class Wearpon(models.Model):
    power = models.IntegerField()
    rerety = models.CharField(max_length=50)
    value = models.IntegerField()



