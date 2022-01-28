from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from modules.questionnaire.api.serializers import SurveyAnswerWriteSerializer, SurveyAnswerReadTreeSerializer
from modules.questionnaire.services import UserService


class AnswerSurveyApi(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request):
        user: User = request.user
        queryset = UserService(user).get_answers()
        return Response(SurveyAnswerReadTreeSerializer(queryset, many=True).data)

    def create(self, request: Request):
        user: User = request.user
        serializer = SurveyAnswerWriteSerializer(data=request.data, context={'user': user})
        serializer.is_valid(raise_exception=True)
        answer_survey = serializer.save()
        return Response(SurveyAnswerReadTreeSerializer(answer_survey).data)

    def retrieve(self, request: Request, pk):
        user: User = request.user
        answer = UserService(user).get_answer(pk)
        return Response(SurveyAnswerReadTreeSerializer(answer).data)
