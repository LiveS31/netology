from django.db import models
from django.contrib.auth.models import User


class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""

    OPEN = 'OPEN', 'Открыто'
    CLOSED = 'CLOSED', 'Закрыто'
    DRAFT = 'DRAFT', 'Черновик'


class Advertisement(models.Model):
    """Объявление."""
# создаем таблицу
    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)