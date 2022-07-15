from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Mobile
from .serializers import MobileSerializer


class HomeView(ListView):
    template_name = "pages/home.html"

    def get_queryset(self):
        return Mobile.objects.filter_active_status()[:6]


class MobileViewSet(ModelViewSet):
    queryset = Mobile.objects.filter_active_status().prefetch_related(
        "category"
    )
    serializer_class = MobileSerializer
    filterset_fields = ["price", "production_date"]
    ordering_fields = ["price", "title"]
    search_fields = [
        "title",
    ]
    ordering = ["-created"]
