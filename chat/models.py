from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Message(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sender",
        verbose_name=_("message sender"),
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="receiver",
        verbose_name=_("message receiver"),
    )
    message = models.CharField(
        max_length=1200,
        verbose_name=_("message"),
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("timestamp"),
    )
    is_read = models.BooleanFeild(
        default=False,
        verbose_name=_("is read"),
    )

    def __str__(self):
        return self.message

    class Meta:
        ordering = ("timestamp",)
