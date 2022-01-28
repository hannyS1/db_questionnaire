from rest_framework import serializers

from .question import QuestionReadTreeSerializer
from modules.questionnaire.models import Survey


class SurveyReadTreeSerializer(serializers.ModelSerializer):
    questions = QuestionReadTreeSerializer(many=True)

    class Meta:
        model = Survey
        fields = [
            'id', 'start_date', 'end_date', 'name', 'questions'
        ]
