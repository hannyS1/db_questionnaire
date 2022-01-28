from io import BytesIO
from typing import Union, Optional, List

from django.contrib.auth.models import User
from django.db.models import Q, QuerySet
from django.template.loader import get_template
from django.utils import timezone
from rest_framework.exceptions import ValidationError, NotFound, APIException
# from django.http import HttpResponse
# from xhtml2pdf import pisa

from modules.questionnaire.models import Survey, AnswerSurvey, Question, AnswerQuestion


class SurveyService:

    def __init__(self, survey: Survey):
        self.survey = survey

    @staticmethod
    def get_active_surveys() -> Union[QuerySet, Survey]:
        now_date = timezone.now().date()
        queryset = Survey.objects.filter(
            ~Q(start_date__gt=now_date) & ~Q(end_date__lt=now_date)
        ).prefetch_related('questions').prefetch_related('questions__choices')

        return queryset

    @staticmethod
    def get_by_id(id: int) -> Survey:
        survey = Survey.objects.filter(id=id).first()
        if not survey:
            raise NotFound(detail='Опрос с данным id не найден')
        return survey

    def get_answers(self):
        return AnswerSurvey.objects.filter(survey=self.survey)


class UserService:
    def __init__(self, user: User):
        self.user = user

    def get_answer(self, pk: int) -> AnswerSurvey:
        answer = AnswerSurvey.objects.filter(id=pk).first()

        if not answer:
            raise NotFound('Ответ не найден')
        if answer.user != self.user:
            raise ValidationError('Ответ не принадлежит этому пользователю')

        return answer

    def get_answers(self) -> Union[QuerySet, AnswerSurvey]:
        return AnswerSurvey.objects.filter(user=self.user)

    def get_accessible_surveys(self) -> Union[QuerySet, Survey]:
        answers_ids_queryset = self.get_answers().values_list('survey_id')
        answers_ids = list(map(lambda x: x[0], answers_ids_queryset))
        return SurveyService.get_active_surveys().exclude(id__in=answers_ids)


# class PdfService:
#
#     @staticmethod
#     def get_pdf_response(template_src: str, context: dict) -> Optional[HttpResponse]:
#         template = get_template(template_src)
#         html = template.render(context)
#         result = BytesIO()
#         pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#         if not pdf.err:
#             return HttpResponse(result.getvalue(), content_type='application/pdf')
#         return None
#
#     @staticmethod
#     def get_survey_answer_data(survey: Survey):
#         questions = Question.objects.filter(survey=survey).prefetch_related('choices')
#         data = dict()
#         data['survey_name'] = survey.name
#         data['questions'] = list()
#         for question in questions:
#
#             question_answers = AnswerQuestion.objects.filter(question=question)
#             question_answers_count = question_answers.count()
#             choices = question.choices
#             data['questions'].append({
#                 'question_text': question.text,
#                 'choices_answers': list()
#             })
#             for choice in choices:
#                 choice_answer = AnswerQuestion.objects.filter(choice=choice)
#                 choice_answer_count = choice_answer.count()
#                 choice_answer_percent = choice_answer_count / question_answers_count * 100
#                 data['questions']['choices_answers'].append({
#
#                 })
#
#     @classmethod
#     def generate_answers_report(cls, surveys: List[Survey]) -> HttpResponse:
#         data = list()
#         for survey in surveys:
#             pass



