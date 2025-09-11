from django.shortcuts import  render, redirect
from mypro.firebase_config import db
from django.contrib import messages

def Contacts(request):
    if request.method=="POST":
        a = request.POST.get("name")
        b = request.POST.get("email")
        c = request.POST.get("message")

        db.collection("contact").add({
            "Name": a,
            "Email" :b,
            "Msg": c
        })
        messages.success(request,"query has been submitted")
        return redirect("con")

    return render(request,"myapp/contact.html")