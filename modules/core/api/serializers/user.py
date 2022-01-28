from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as RestValidationError
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

    def create(self, validated_data):
        password = validated_data.get('password', None)
        username = validated_data.get('username', None)

        if User.objects.filter(username=username).exists():
            raise RestValidationError('Пользователь с таким именем уже существует')

        try:
            password_validation.validate_password(password)
        except ValidationError as err:
            raise RestValidationError(err.messages)

        hashed_password = make_password(password)

        return User.objects.create(
            username=username,
            password=hashed_password,
            is_active=True,
        )
