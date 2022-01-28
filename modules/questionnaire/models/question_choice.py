from django.db import models
from .question import Question


class QuestionChoice(models.Model):
    question = models.ForeignKey(
        to=Question,
        on_delete=models.CASCADE,
        related_name='choices',
        verbose_name='Вопрос'
    )
    text = models.CharField(
        max_length=255,
        verbose_name='Текст варианта'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'
