from django.urls import path
from .views import SendOTPAPIView, VerifyOTPAPIView


urlpatterns = [
    path("send/", SendOTPAPIView.as_view(), name="send"),
    path("verify/", VerifyOTPAPIView.as_view(), name="verify"),
]
