from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class AuthorizationValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegistrationValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    is_active = serializers.BooleanField(default=False)

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')