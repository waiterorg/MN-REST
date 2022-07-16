from django.urls import path
from rest_framework import routers

from .views import HomeView, ListMobile

urlpatterns = [
    path("mobiles/", ListMobile.as_view()),
]
