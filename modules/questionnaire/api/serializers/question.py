from rest_framework import serializers
from .question_choice import QuestionChoiceReadTreeSerializer

from modules.questionnaire.models import Question


class QuestionReadTreeSerializer(serializers.ModelSerializer):
    choices = QuestionChoiceReadTreeSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            'id', 'text', 'choices'
        ]
