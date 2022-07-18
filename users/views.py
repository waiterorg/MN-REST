from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ChangePasswordSerializer, UserSerializer


class RegisterView(APIView):
    """
    An endpoint for register user .
    """

    http_method_names = ["post"]

    def post(self, *args, **kwargs):
        serializer = UserSerializer(data=self.request.data)
        if serializer.is_valid():
            get_user_model().objects.create_user(**serializer.validated_data)
            return Response(
                status=status.HTTP_201_CREATED,
                data={"message": "user created !"},
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={"errors": serializer.errors},
        )


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing user password .
    """

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(
                serializer.data.get("old_password")
            ):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()

            return Response(
                status=status.HTTP_200_OK,
                data={"message": "Password updated successfully"},
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
