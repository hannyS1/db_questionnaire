from django import forms
from django.forms import TextInput
from nested_admin import nested
from django.contrib import admin

from .models import Survey, Question, QuestionChoice, AnswerQuestion, AnswerSurvey


class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'text': TextInput(attrs={'size': 70})
        }


class QuestionChoiceAdminForm(forms.ModelForm):
    class Meta:
        model = QuestionChoice
        fields = '__all__'
        widgets = {
            'text': TextInput(attrs={'size': 70})
        }


class SurveyAdminForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'size': 70})
        }


class QuestionChoiceInline(nested.NestedStackedInline):
    model = QuestionChoice
    form = QuestionChoiceAdminForm
    extra = 0


class QuestionInline(nested.NestedStackedInline):
    model = Question
    form = QuestionAdminForm
    extra = 0

    inlines = [QuestionChoiceInline]


@admin.register(Survey)
class SurveyAdmin(nested.NestedModelAdmin):

    list_display = [
        'id', 'name', 'start_date', 'end_date'
    ]

    model = Survey
    form = SurveyAdminForm
    inlines = [QuestionInline]


@admin.register(AnswerQuestion)
class AnswerQuestion(admin.ModelAdmin):

    list_filter = ['question__survey']
    list_per_page = 25
