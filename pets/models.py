from django.db import models
from datetime import datetime
from PIL import Image
import os
from shelters.models import Shelter  # Adjust as needed
from .choices import STATES

class Pet(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    pet_type = models.CharField(max_length=100, choices=[
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Rabbit', 'Rabbit'),
        ('Bird', 'Bird'),
        ('Other', 'Other')
    ])
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    age = models.IntegerField()
    size = models.CharField(max_length=50, choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
    state = models.CharField(max_length=100, choices=STATES, default='anywhere')  # New field
    vaccinated = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False, null=False)  # Mandatory
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    # add more photos if needed
    is_adopted = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # First, save the model so the file gets uploaded
        super().save(*args, **kwargs)
       

    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"
