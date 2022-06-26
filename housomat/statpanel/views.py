from rest_framework import viewsets
from rest_framework import permissions
from .models import TempReading
from .serializer import TempReadingSerializer


class TempReadingViewSet(viewsets.ModelViewSet):
    queryset = TempReading.objects.all()
    serializer_class = TempReadingSerializer
    permission_classes = [permissions.AllowAny]