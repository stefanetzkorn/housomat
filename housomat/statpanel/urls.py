from django.urls import path, include
from rest_framework import routers
from .views import TempReadingViewSet


router = routers.DefaultRouter()
router.register(r'tempreading', TempReadingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
