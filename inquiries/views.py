from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Inquiry
from pets.models import Pet

def add_inquiry(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save inquiry in the database
        inquiry = Inquiry.objects.create(pet=pet, name=name, email=email, message=message)

        # ✅ Email to user (confirmation)
        send_mail(
            subject="Inquiry Received - Adoptify",
            message=f"Hello {name},\n\nThank you for your inquiry about {pet.name}. We will get back to you shortly.\n\nBest regards,\nAdoptify Team",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        # ✅ Email to admin (notification)
        admin_email = settings.ADMIN_NOTIFICATION_EMAIL  # You can hardcode a specific email if needed
        send_mail(
            subject=f"New Inquiry Submitted on Adoptify",
            message=f"New inquiry details:\n\nName: {name}\nEmail: {email}\nPet: {pet.name}\nMessage:\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[admin_email],
            fail_silently=False,
        )

        messages.success(request, "Your inquiry has been submitted successfully.")
        return redirect("pet_detail", pet_id=pet.id)

    return render(request, "inquiries/inquiry_form.html", {"pet": pet})
