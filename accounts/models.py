from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    PET_EXPERIENCE_CHOICES = [
        ('beginner', 'Beginner - No experience'),
        ('some_experience', 'Some experience'),
        ('experienced', 'Experienced'),
        ('expert', 'Expert - Have owned many pets'),
    ]
    
   
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pet_experience = models.CharField(
        max_length=20, choices=PET_EXPERIENCE_CHOICES, default='beginner')

    def __str__(self):
        return self.username
