from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """
    Custom user model includes unique username, email and phone number .
    """

    username = models.CharField(
        verbose_name=_("username"), max_length=255, unique=True
    )
    email = models.EmailField(verbose_name=_("email address"), unique=True)
    phone = PhoneNumberField(
        verbose_name=_("phone number"),
        null=True,
        blank=True,
        max_length=20,
        unique=True,
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
