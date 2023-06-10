from django.db import models
from django.contrib.auth.models import User
#создаем такблицу для коментаря на сайте
class Comment(models.Model):
    # Cоздаем поле USER с внешним ключем
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Создаем TEXT без ограничения по символам
    text = models.TextField()
    # Создаем для записи даты и время для регистрации сообшения
    create_at = models.DateTimeField(auto_now_add=True)