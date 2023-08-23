from django.contrib import admin
from django.urls import path, include

from authorization.views import SendPhone, SendCode

urlpatterns = [
    path('phone/', SendPhone.as_view()),
    path('', SendCode.as_view()),
]
