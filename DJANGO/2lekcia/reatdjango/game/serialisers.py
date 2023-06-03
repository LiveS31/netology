#импортируем из нашей бублиотеки serializers
from rest_framework import serializers
from .models import Wearpon
# тут будем переводить на доступный язык для django

# class WeaponSerializer(serializers.Serializer): # создаем класс настледующийся от Serializer
#     # описываем свойства которые длжны быть сконвертированы в json
#     #  и наоборот в сложный обЪект
#     power = serializers.IntegerField() # потому что он в цифрах
#     rerety = serializers.CharField() # потому что он буквенный

#если serializers - повторяет модель, то можно использовать специальный класс

class WeaponSerializer(serializers.ModelSerializer):
    # Наследуемся от ModelSerializer.
# Требуется указать на основании какой модели будет создан serializer
# возьмет все свойства модели и сгенерирует автоматически:
    #power = serializers.IntegerField()
    #rerety = serializers.CharField()
# Для того, чтобы указать от какого класса наследуется
# нужно создать класс мета и указать
    class Meta:
        model = Wearpon #клас от которого принимает данные
        # Указываем список свойств, которые необходимо отобрать
        fields = ['id', 'power', 'rerety'] # список свойств для отображения
        #добавили поле id для получения информации о номере оружия