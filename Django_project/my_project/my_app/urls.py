from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index,name="Index"),
    path("a", views.About,name="about"),
    path("c", views.Contact,name="contact"),
]