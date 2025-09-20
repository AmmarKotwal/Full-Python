from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.Contacts, name="con"),
    path("show",views.ShowData, name="show"),
    path("show/del/<str:id>", views.Delete, name="delcon"),
    path("r", views.register, name="reg")

]