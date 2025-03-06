from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from pets.models import Pet
from .forms import InquiryForm

def add_inquiry(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.pet = pet
            inquiry.save()
            messages.success(request, 'Your inquiry has been submitted')
            return redirect('pet_detail', pet_id=pet.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = InquiryForm()
    context = {
        'pet': pet,
        'form': form,
    }
    return render(request, 'inquiries/add_inquiry.html', context)
