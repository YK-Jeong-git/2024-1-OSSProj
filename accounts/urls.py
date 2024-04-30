from django.contrib import admin
from django.urls import path, include

from accounts.views import sign_up

urlpatterns = [
    path('sign_up/', sign_up)
]