from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""

    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"


class Advertisement(models.Model):
    """Объявление."""
#создаем таблицу
    title = models.TextField()
    description = models.TextField(default='')# текст объявления
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    ) #статус объявления
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    creator_at = models.DateTimeField(
        auto_now_add=True #дата автоматом
    )
    update_at = models.DateTimeField(
        auto_now=True #дата автоматом
    )
    def __str__(self):
        return self.title

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
