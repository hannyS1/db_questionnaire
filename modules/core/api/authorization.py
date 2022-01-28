from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from config.settings import logger
from modules.core.api.serializers import UserSerializer


class AuthorizationApi(viewsets.ViewSet):

    permission_classes = [AllowAny]

    @action(methods=['post'], detail=False)
    def register(self, request: Request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)

        return Response({'token': token.key})

    @action(methods=['post'], detail=False)
    def login(self, request: Request):
        username = request.data.get('username')
        password = request.data.get('password')
        user: User = User.objects.filter(username=username).first()

        if not user or not check_password(password, user.password):
            return Response('Логин и пароль не совпадают', status=status.HTTP_400_BAD_REQUEST)

        token = Token.objects.filter(user=user).first()
        if not token:
            token = Token.objects.create(user=user)

        logger.info(f'user {username} auth')

        return Response({'token': token.key})

    @action(methods=['get'], detail=False, url_path='user-info')
    def user_info(self, request: Request):
        user: User = request.user
        logger.debug(f'user: {user.username}')
        return Response(UserSerializer(user).data)
