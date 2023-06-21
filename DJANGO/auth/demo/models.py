from django.contrib.auth.models import User #Импортируем пользователя

from django.db import models


class Adv(models.Model):# создаем таблицу
    #создаем пользователя USER и импортируем его
    user = models.ForeignKey(User, on_delete=models.CASCADE)#создаем правило удаления
#пользователя каскадно - это обязательное условие

    #создаем текст
    text = models.TextField()

    # Создаем время создания записи если его не прописали
    created_at = models.DateTimeField(auto_now_add=True)# время создастся автоматичеси
    # если его не указать

    #поумолчанию состояние обЪявлеия будет TRUE(открытым)
    open = models.BooleanField(default=True)