
from django.contrib import admin
from django.urls import path, include
from django.conf import  settings
from api import views
urlpatterns = [
    path('attractions/', views.AttractionAPIView.as_view(), name='attractions'),

]
