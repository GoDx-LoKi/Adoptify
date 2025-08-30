
# Create your models here.
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 

class Shelter(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


class ShelterApplication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shelter_name = models.CharField(max_length=100,null=True, blank=True)
    location = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shelter_name} - {self.user.username}"