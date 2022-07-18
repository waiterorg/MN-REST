from django.urls import path

from .views import ListMobile

urlpatterns = [
    path("mobiles/", ListMobile.as_view()),
]
