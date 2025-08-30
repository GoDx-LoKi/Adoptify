from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ShelterApplicationForm

@login_required
def become_shelter(request):
    if request.method == "POST":
        form = ShelterApplicationForm(request.POST)
        if form.is_valid():
            shelter_app = form.save(commit=False)
            shelter_app.user = request.user
            shelter_app.save()
            messages.success(request, "Your shelter application has been submitted!")
            return redirect("home")
    else:
        form = ShelterApplicationForm()
    return render(request, "shelters/become_shelter.html", {"form": form})
