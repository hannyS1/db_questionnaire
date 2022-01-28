from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .question_answer import QuestionAnswerReadTreeSerializer, QuestionAnswerWriteSerializer
from ...models import AnswerSurvey, Survey, AnswerQuestion


class SurveyAnswerReadTreeSerializer(serializers.ModelSerializer):

    survey_name = serializers.CharField(source='survey.name')
    survey_id = serializers.IntegerField(source='survey.id')
    questions_answers = QuestionAnswerReadTreeSerializer(many=True)

    class Meta:
        model = AnswerSurvey
        fields = [
            'id', 'survey_id', 'survey_name', 'questions_answers'
        ]


class SurveyAnswerWriteSerializer(serializers.ModelSerializer):

    survey_id = serializers.CharField(write_only=True)
    questions_answers = QuestionAnswerWriteSerializer(write_only=True, many=True)

    class Meta:
        model = AnswerSurvey
        fields = [
            'survey_id', 'questions_answers'
        ]

    @transaction.atomic
    def create(self, validated_data):
        survey_id = validated_data.get('survey_id')
        questions_answers = validated_data.get('questions_answers')
        survey: Survey = Survey.objects.filter(id=survey_id).first()
        user: User = self.context.get('user', None)
        question_answer_list = list()

        if not user:
            raise ValidationError('Не передан пользователь, который проходил опрос')

        if not survey:
            raise ValidationError('Опрос с данным id не найден')

        answer_survey = AnswerSurvey.objects.create(user=user, survey=survey)

        for question_answer in questions_answers:
            serializer = QuestionAnswerWriteSerializer(data=question_answer, context={'answer_survey': answer_survey})
            serializer.is_valid(raise_exception=True)
            question_answer_obj = serializer.save()
            question_answer_list.append(question_answer_obj)

        try:
            AnswerQuestion.objects.bulk_create(question_answer_list)
        except Exception as err:
            raise ValidationError('invalid data')

        return answer_survey
