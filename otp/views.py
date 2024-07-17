from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from .settings import OTP_SETTINGS
from .extentions import send_otp
from .models import OTPRequest
from .serializers import (
    SendOTPRequestSerializer,
    SendOTPResponseSerializer,
    VerifyOTPRequestSerializer,
    JWTVerifyOTPResponseSerializer,
    SimpleTokenVerifyOTPResponseSerializer
)

if OTP_SETTINGS.JWT_Authentication:
    try:
        from rest_framework_simplejwt.tokens import RefreshToken
    except:
        raise Exception("'rest_framework_simplejwt' dose not installed.")
else:
    from rest_framework.authtoken.models import Token


class SendOTPAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = SendOTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                otp = OTPRequest.objects.generate(data)
                send_otp(otp)
                return Response(
                    data=SendOTPResponseSerializer(instance=otp).data,
                    status=status.HTTP_201_CREATED
                )
            except Exception as err:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = VerifyOTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            if OTPRequest.objects.is_valid(**data):
                otp = OTPRequest.objects.get(**data)
                return self._handle_login(request, otp)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_serializer(self):
        if OTP_SETTINGS.JWT_Authentication:
            return JWTVerifyOTPResponseSerializer
        return SimpleTokenVerifyOTPResponseSerializer
    
    def _get_key(self, otp):
        if (
            OTP_SETTINGS.SEND_OTP_TO_PHONE and
            otp.channel == "Phone" and
            OTP_SETTINGS.USER_PHONE_ATTR
        ):
            key = OTP_SETTINGS.USER_PHONE_ATTR
        elif (
            OTP_SETTINGS.SEND_OTP_TO_EMAIL and
            otp.channel == "EMail" and
            OTP_SETTINGS.USER_EMAIL_ATTR
        ):
            key = OTP_SETTINGS.USER_EMAIL_ATTR
        else:
            key = OTP_SETTINGS.USER_DEFAULT_ATTR
        return key
    
    def _get_response_data(self, user, created):
        if OTP_SETTINGS.JWT_Authentication:
            refresh = RefreshToken.for_user(user=user)
            return dict(
                access=str(refresh.access_token),
                refresh=str(refresh),
                created=created
            )
        token, is_created = Token.objects.get_or_create(user=user)
        return dict(
            token=token,
            created=created
        )
    
    def _handle_login(self, request, otp):
        key = self._get_key(otp=otp)
        try:
            user, created = get_user_model().objects.get_or_create(**{key: otp.receiver})
            login(request, user)
            serializer = self.get_serializer()
            instance = self._get_response_data(user=user, created=created)
            return Response(data=serializer(instance=instance).data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
