from django.urls import path
from form_exmple import views

urlpatterns = [
    path("contact/", views.contact, name="contact"),
]
