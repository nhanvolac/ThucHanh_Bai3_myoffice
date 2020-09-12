from django.shortcuts import render
from . import forms

# Create your views here.

def about(request):
    return render(request, "officemaster/about.html")

def blog(request):
    return render(request, "officemaster/blog.html")

def contact(request):
    registered = False
    if request.method == "POST":
        form_contact = forms.FormContact(data = request.POST) 
        if form_contact.is_valid():
            register = form_contact.save()
            register.save()
            registered = True
        else:
            print(form_contact.errors)
    else:
        form_contact = forms.FormContact()

    return render(request, "officemaster/contact.html",{'contact_form':form_contact,'registered': registered})

def team(request):
    return render(request, "officemaster/team.html")

def index(request):
    return render(request, "officemaster/index.html")
