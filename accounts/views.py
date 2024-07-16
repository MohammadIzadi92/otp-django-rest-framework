from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
from random import randint
from .extentions import send_otp, get_channel
from .models import OTPRequest, CustomUser
from .serializers import (
    LoginRequestSerializer,
    LoginResponseSerializer,
    VerifyRequestSerializer,
    VerifyResponseSerializer
)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                otp = OTPRequest.objects.generate(data)
                send_otp(otp)
                return Response(
                    data=LoginResponseSerializer(instance=otp).data,
                    status=status.HTTP_201_CREATED
                )
            except Exception as err:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = VerifyRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            if OTPRequest.objects.is_valid(**data):
                return Response(data=self._handle_login(data), status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def _handle_login(self, otp):
        if get_channel(otp["receiver"]) == "Phone":
            data = dict(phone_number=otp["receiver"])
        else:
            data = dict(email=otp["receiver"])
        user, created = CustomUser.objects.get_or_create(**data)
        refresh = RefreshToken.for_user(user=user)
        return VerifyResponseSerializer(
            instance=dict(
                access=str(refresh.access_token),
                refresh=str(refresh),
                created=created
            )
        ).data