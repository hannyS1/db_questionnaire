from django.db import models

from .survey import Survey


class Question(models.Model):
    text = models.CharField(
        max_length=255,
        verbose_name='Текст вопроса'
    )
    survey = models.ForeignKey(
        to=Survey,
        on_delete=models.CASCADE,
        verbose_name='Опрос',
        related_name='questions'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
