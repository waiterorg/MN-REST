from django.db.models import Q

from ..models import Message


def get_user_messages(user):
    message = Message.objects.filter(Q(sender=user) | Q(receiver=user))
    return message


def send_user_messages(user, receiver, message):
    message = Message.objects.create(
        sender=user,
        receiver=receiver,
        message=message,
    )
    return message
