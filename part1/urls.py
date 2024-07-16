from django.urls import path
from . import views

app_name = "part1"

urlpatterns = [
    path("current_datetime", views.current_datetime, name="current_datetime"),
    path("hours/", views.hours_4, name="4_hours"),
    path("olul/", views.olul, name="olul"),
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
]
