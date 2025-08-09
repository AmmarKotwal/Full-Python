from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, "my_app/Index.html")

def About(request):
    return render(request, "my_app/About.html")

def Contact(request):
    return render(request, "my_app/Contact.html")