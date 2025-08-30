from django.urls import path
from . import views

urlpatterns = [
    path("become/", views.become_shelter, name="become_shelter"),
]
