from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from modules.questionnaire.api.serializers import QuestionReadTreeSerializer, QuestionChoiceReadTreeSerializer
from modules.questionnaire.models import AnswerQuestion


class QuestionAnswerReadTreeSerializer(serializers.ModelSerializer):

    question = QuestionReadTreeSerializer()

    class Meta:
        model = AnswerQuestion
        fields = [
            'id', 'choice', 'question'
        ]


class QuestionAnswerWriteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()
    question_id = serializers.IntegerField()

    def create(self, validated_data):
        answer_survey = self.context.get('answer_survey')

        if not answer_survey:
            raise ValidationError('Не передан ответ на опрос')

        return AnswerQuestion(**validated_data, answer_survey=answer_survey)


