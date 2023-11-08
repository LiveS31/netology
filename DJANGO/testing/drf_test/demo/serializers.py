from rest_framework import serializers

from .models import Message

#создаем класс и наследуем его вышестоящего
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        # указываем на основании чего создается данный serializers
        model = Message
        #прописываем используемые поля
        fields = ['id', 'user', 'text', 'created_at']
