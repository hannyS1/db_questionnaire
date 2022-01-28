from django.contrib.auth.models import User
from django.db import models
from .survey import Survey


class AnswerSurvey(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        verbose_name='Пользователь',
        null=True
    )
    survey = models.ForeignKey(
        to=Survey,
        on_delete=models.CASCADE,
        verbose_name='Опрос'
    )

    def __str__(self):
        if not self.user:
            return str(self.survey)
        return f'{str(self.user)}: {str(self.survey)}'

    class Meta:
        verbose_name = 'Ответ пользователя на опрос'
        verbose_name_plural = 'Ответы пользователя на опросы'
