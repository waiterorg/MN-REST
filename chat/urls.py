from django.urls import path

from .views import MessageList

urlpatterns = [
    path("message/", MessageList.as_view()),
]
