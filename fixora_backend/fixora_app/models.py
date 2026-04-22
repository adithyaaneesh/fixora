from django.db import models

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.service_name
    
class Booking(models.Model):
    _status = models.CharField(max_length=20, default='true')