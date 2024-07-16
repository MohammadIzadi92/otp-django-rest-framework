from rest_framework import serializers
from .models import CustomUser, OTPRequest


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class LoginRequestSerializer(serializers.Serializer):
    receiver = serializers.CharField(max_length=50, allow_null=False)


class LoginResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTPRequest
        fields = ["request_id"]


class VerifyRequestSerializer(serializers.Serializer):
    request_id = serializers.UUIDField(allow_null=False)
    password = serializers.CharField(max_length=6)
    receiver = serializers.CharField(max_length=50, allow_null=False)


class VerifyResponseSerializer(serializers.Serializer):
    access = serializers.CharField(max_length=500, allow_null=False)
    refresh = serializers.CharField(max_length=500, allow_null=False)
    created = serializers.BooleanField()
