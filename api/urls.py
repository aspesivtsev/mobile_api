
from django.contrib import admin
from django.urls import path, include
from django.conf import  settings
from api import views

app_name = 'api'
urlpatterns = [
    path('attractions/', views.AttractionAPIView.as_view(), name='attractions'),

]
