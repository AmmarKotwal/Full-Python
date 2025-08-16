from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.Home, name="home"),
    path("a", views.About, name="about"),
    path("cs", views.Courses, name="courses"),
    path("c", views.Contact, name="contact"),
]