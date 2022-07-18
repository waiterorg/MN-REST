from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class UsernameOrPhoneOrEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        """
        Custom authentication with username or email or phone number .
        """
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(
                Q(username=username) | Q(email=username) | Q(phone=username)
            )
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
        return None
