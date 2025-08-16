from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, "my_app/Home.html")

def About(request):
    return render(request, "my_app/About.html")

def Courses(request):
    return render(request, "my_app/Courses.html")

def Contact(request):
    return render(request, "my_app/Contact.html")
