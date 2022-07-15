from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class HomeView(ListView):
    template_name = "pages/home.html"

    def get_queryset(self):
        return Product.objects.filter_active_status()[:6]
