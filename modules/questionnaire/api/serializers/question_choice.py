from rest_framework import serializers

from modules.questionnaire.models import QuestionChoice


class QuestionChoiceReadTreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionChoice
        fields = [
            'id', 'text'
        ]
