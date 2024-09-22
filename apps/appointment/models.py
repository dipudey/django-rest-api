from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(null=True, blank=True)
    phone= models.CharField(max_length=20)
    email = models.EmailField(null=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)