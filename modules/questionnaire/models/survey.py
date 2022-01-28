from django.utils import timezone
from django.db import models


class Survey(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    start_date = models.DateField(
        verbose_name='Начало опроса',
        null=True,
        blank=True
    )
    end_date = models.DateField(
        verbose_name='Окончание опроса',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
