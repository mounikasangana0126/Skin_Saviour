from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from home.views import HomeAPI

urlpatterns = [
    path('', HomeAPI, name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
]
