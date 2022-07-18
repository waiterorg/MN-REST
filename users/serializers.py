from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user endpoint .
    """

    class Meta:
        model = get_user_model()
        fields = ("email", "username", "password")


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint .
    """

    model = get_user_model()

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
