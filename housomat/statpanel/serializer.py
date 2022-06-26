from .models import TempReading
from rest_framework import serializers

class TempReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempReading
        fields = "__all__"