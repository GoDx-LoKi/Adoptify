from django import forms
from .models import ShelterApplication

class ShelterApplicationForm(forms.ModelForm):
    class Meta:
        model = ShelterApplication
        fields = ['shelter_name', 'location', 'email', 'phone', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
