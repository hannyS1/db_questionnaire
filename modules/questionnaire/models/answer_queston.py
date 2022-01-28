from django.db import models

from .question import Question
from .answer_survey import AnswerSurvey
from .question_choice import QuestionChoice


class AnswerQuestion(models.Model):
    question = models.ForeignKey(
        to=Question,
        on_delete=models.CASCADE,
        verbose_name='Вопрос'
    )
    answer_survey = models.ForeignKey(
        to=AnswerSurvey,
        on_delete=models.CASCADE,
        related_name='questions_answers',
        verbose_name='Ответ на опрос'
    )
    choice = models.ForeignKey(
        to=QuestionChoice,
        on_delete=models.CASCADE,
        verbose_name='Выбор ответа'
    )

    def __str__(self):
        return f'{str(self.answer_survey.user)}: {str(self.question.text)}'

    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'
