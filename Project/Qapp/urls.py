from django.contrib import admin
from django.urls import path, include
from .views import home, quiz, result

urlpatterns = [
    path('', home, name='home'),
    path('quiz/<int:pk>', quiz, name='quiz'),
    path('result/<int:pk>', result, name='result'),
]
