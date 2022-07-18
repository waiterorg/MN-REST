from django.urls import path

from .views import ChangePasswordView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="token_obtain_pair"),
    path(
        "change-password/",
        ChangePasswordView.as_view(),
        name="change-password",
    ),
]
