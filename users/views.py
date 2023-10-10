from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from random import choices
from .serializers import AuthorizationValidateSerializer, RegistrationValidateSerializer
from .utils import send_email
from .models import Confirm


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegistrationValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data)

        code = ''.join(choices('0123456789', k=6))
        Confirm.objects.create(code=code, user=user)

        subject = 'Confirm code'
        message = f'http://127.0.0.1:8000/api/v1/users/confirm?code={code}'
        recipient_list = [user.email]
        send_email(subject, message, recipient_list)

        return Response(data={'user_id': user.id, 'message': message}, status=status.HTTP_201_CREATED)


class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = AuthorizationValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_403_FORBIDDEN)


class ConfirmAPIView(APIView):
    def get(self, request):
        try:
            code = request.GET.get('code')
            user = Confirm.objects.get(code=code).user
            user.is_active = True
            user.save()
        except Confirm.DoesNotExist:
            return Response(data={'error': 'Code is not valid!'})
        return Response(status=status.HTTP_202_ACCEPTED)
