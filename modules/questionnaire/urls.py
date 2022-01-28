from django.urls import path, include
from rest_framework.routers import DefaultRouter

from modules.questionnaire.api import SurveyApi, AnswerSurveyApi

router = DefaultRouter()
router.register('survey', SurveyApi, basename='auth')
router.register('answer-survey', AnswerSurveyApi, basename='answer-survey')

urlpatterns = [
    path('', include(router.urls)),
]
