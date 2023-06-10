from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Comment
class CommentSerializer(serializers.ModelSerializer):
    #ненужно выводить текст менее 10 символов
    text = serializers.CharField(min_length=10)
    class Meta:
        model = Comment # модель это таблица Comment
        #Коментарии которые будут отображаться
        fields = ['id', 'user', 'text', 'created_at']

    # если нужно, чтобы не было каких либо слов(например запрщнных)

    def validate_text(self, value):  #_text - поле которое нужно проверить
        if 'text' in value:
            raise ValidationError('Вы использовали заперщенное слово')
#если слово text встречается в value, то вывесли ошибку на экран
        return value

#если нужно несколько полей, то нужно использовать
    def validate(self, attrs):
        if 'hello' in attrs['text'] or attrs['user'].id == 1:
            raise ValidationError('Что -то не так')
        return attrs #возвращаем если все ок

#serializers - создание и обновение объектов

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)
