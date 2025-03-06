from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:pet_id>/', views.add_inquiry, name='add_inquiry'),
]