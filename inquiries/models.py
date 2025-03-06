from django.db import models
from pets.models import Pet

class Inquiry(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Inquiry for {self.pet.name} by {self.name}'
