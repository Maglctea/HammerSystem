from django.contrib import admin
from django.urls import path, include

from user.views import UserProfile

urlpatterns = [
    path('profile/', UserProfile.as_view()),
]
