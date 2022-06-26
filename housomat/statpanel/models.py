from django.db import models

# Create your models here.

class TempReading(models.Model):
    temp = models.FloatField()
    date = models.DateTimeField()

    def to_fahrenheit(self):
        return self.temp * 9/5 + 32
    
    def __str__(self):
        return f"{self.temp} - {self.dates}"