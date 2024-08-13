"""Defines URL patterns for autho_app"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('registration/', views.topics, name='registration'),
    path('authentication/', views.authentication, name='authentication'),
]