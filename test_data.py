import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from modules.questionnaire.models import Survey, Question, QuestionChoice
from django.contrib.auth.models import User


def create_users():
    User.objects.create_superuser(
        username='admin',
        password='123'
    )
    User.objects.create_user(
        username='roma356',
        password='08022001q'
    )


def create_surveys():
    survey1 = Survey.objects.create(
        name='Общий'
    )
    question11 = Question.objects.create(
        survey=survey1,
        text='Как у вас дела?'
    )
    choices111 = QuestionChoice.objects.create(
        question=question11,
        text='Хорошо'
    )
    choices112 = QuestionChoice.objects.create(
        question=question11,
        text='Сойдет'
    )
    choices113 = QuestionChoice.objects.create(
        question=question11,
        text='Плохо'
    )
    question12 = Question.objects.create(
        survey=survey1,
        text='Как в целом жизнь?'
    )
    choices121 = QuestionChoice.objects.create(
        question=question12,
        text='Супер'
    )
    choices122 = QuestionChoice.objects.create(
        question=question12,
        text='Не Супер'
    )
    choices123 = QuestionChoice.objects.create(
        question=question12,
        text='Ужасно'
    )


def create_all():
    create_users()
    create_surveys()


if __name__ == '__main__':
    create_all()
