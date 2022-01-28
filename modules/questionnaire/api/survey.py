from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from modules.questionnaire.api.serializers import SurveyReadTreeSerializer
from modules.questionnaire.services import SurveyService, UserService


class SurveyApi(viewsets.ViewSet):

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]

        return super(SurveyApi, self).get_permissions()

    def list(self, request: Request):
        if request.user.is_authenticated:
            queryset = UserService(request.user).get_accessible_surveys()
        else:
            queryset = SurveyService.get_active_surveys()

        serializer = SurveyReadTreeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: Request, pk: int):
        survey = SurveyService.get_by_id(pk)
        serializer = SurveyReadTreeSerializer(survey)
        return Response(serializer.data)
