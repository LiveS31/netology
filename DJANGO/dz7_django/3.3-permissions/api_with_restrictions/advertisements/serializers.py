from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError #по проверке "слов"
# на несоответствие, ошибки
from .models import Advertisement, Favorite


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        if data.get('status') == None or data.get('status') == 'OPEN':
            creator = self.context['request'].user
            advertisements = Advertisement.objects.all()
            if advertisements.filter(status='OPEN', creator=creator).count() >=10:
                raise ValidationError('Запрос превыcил 10 раз')
        # TODO: добавьте требуемую валидацию

        return data
class FavoriteSerializer(serializers.ModelSerializer):
    advertisement = AdvertisementSerializer()
    class Meta:
        model = Favorite
        fields = ('user', 'advertisement')