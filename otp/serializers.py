from rest_framework import serializers
from .settings import OTP_SETTINGS
from .models import OTPRequest


class SendOTPRequestSerializer(serializers.Serializer):
    receiver = serializers.CharField(max_length=150, allow_null=False)


class SendOTPResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTPRequest
        fields = ["request_id"]


class VerifyOTPRequestSerializer(serializers.Serializer):
    request_id = serializers.UUIDField(allow_null=False)
    password = serializers.CharField(max_length=OTP_SETTINGS.OTP_LENGTH)
    receiver = serializers.CharField(max_length=150, allow_null=False)


class JWTVerifyOTPResponseSerializer(serializers.Serializer):
    access = serializers.CharField(max_length=500, allow_null=False)
    refresh = serializers.CharField(max_length=500, allow_null=False)
    created = serializers.BooleanField()


class SimpleTokenVerifyOTPResponseSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=500, allow_null=False)
    created = serializers.BooleanField()
