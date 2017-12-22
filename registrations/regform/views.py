# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Application
from .forms import ApplicationForm
from django.views.generic.edit import CreateView, UpdateView,DeleteView

# Create your views here.

def home(request):
	return render(request, 'regform/home.html')

def totalregs(request):
	regforms = Application.objects.all()
	context={'regforms':regforms}
   
	return render(request, 'regform/totalregs.html',context)

def registration(request):
	return render(request, 'regform/regform.html')

def login(request):
	return render(request, 'regform/login.html')

def application_new(request):
    form = ApplicationForm()
    return render(request, 'regform/regform.html', {'form': form})


def login(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = Loginform()

    return render(request, 'loggedin.html', {"username": username})





