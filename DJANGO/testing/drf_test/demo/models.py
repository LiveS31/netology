from django.contrib.auth.models import User
from django.db import models

#создаем таблицу с сообщениями от пользователя
class Message(models.Model):
    #пользователь
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #текст сообщения
    text = models.TextField()
    #время создания сообщения с автоматическим заполнением
    created_at = models.DateTimeField(auto_now_add=True)
