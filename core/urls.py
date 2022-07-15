from django.urls import path
from rest_framework import routers

from .views import HomeView, MobileViewSet

router = routers.DefaultRouter()
router.register("mobile", MobileViewSet, basename="mobiles")

urlpatterns = [
    path("", HomeView.as_view()),
]

urlpatterns += router.urls
