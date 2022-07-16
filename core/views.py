from urllib import request

from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .custom_api_view.gen_api_view import CustomGenericAPIView
from .models import Mobile
from .serializers import MobileSerializer


class HomeView(ListView):
    """
    Home page show 6 mobile items
    """

    template_name = "pages/home.html"

    def get_queryset(self):
        return Mobile.objects.filter_active_status()[:6]


class ListMobile(CustomGenericAPIView):
    """
    ListMobile View with active mobile items , filterset, ordering and search field
    """

    serializer_class = MobileSerializer
    filterset_fields = ["price", "production_date"]
    ordering_fields = ["price", "title", "production_date"]
    search_fields = ["title", "category__title"]

    def get_queryset(self):
        mobiles = Mobile.objects.filter_active_status().prefetch_related(
            "category"
        )
        return mobiles

    def get(self, request):

        queryset = self.get_queryset()
        filtered_queryset = self.check_authentication_for_filter_objects(
            queryset
        )
        paginated_queryset = self.paginate_queryset(filtered_queryset)
        serializer = self.check_pagination_page(
            paginated_queryset, filtered_queryset
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
