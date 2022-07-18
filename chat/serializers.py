from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Message


class UserMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for user used in message endpoint .
    """

    class Meta:
        model = get_user_model()
        fields = ["username"]


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for message endpoint .
    """

    sender = serializers.SlugRelatedField(
        many=False,
        slug_field="username",
        queryset=get_user_model().objects.all(),
    )
    receiver = serializers.SlugRelatedField(
        many=False,
        slug_field="username",
        queryset=get_user_model().objects.all(),
    )

    class Meta:
        model = Message
        fields = [
            "sender",
            "receiver",
            "message",
            "timestamp",
        ]
