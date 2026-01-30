from django.db import models

from user.models import CustomUser


class Subscriber(models.Model):
    """Модель «Получатель рассылки»"""

    full_name = models.CharField(max_length=255, verbose_name="Ф.И.О.")
    email = models.EmailField(unique=True, verbose_name="Почта")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="subscriber_owner", default=1)

    def __str__(self):
        return self.full_name
