from django.db import models

class Message(models.Model):
    """Модель «Сообщение»"""

    subject = models.CharField(max_length=255, verbose_name="Тема письма")
    body = models.TextField(null=True, blank=True, verbose_name="Тело письма")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего обновления")

    def __str__(self):
        return self.subject