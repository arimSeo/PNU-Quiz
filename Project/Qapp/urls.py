from django.contrib import admin
from django.urls import path, include
from .views import home, quiz, result, save_ans

urlpatterns = [
    path('', home, name='home'),
    path('quiz/', quiz, name='quiz'),
    path('result/', result, name='result'),
    path('save_ans/', save_ans, name='saveans'),
]
