# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import EmailMessage

from django.shortcuts import render
from basicapp.models import *
from . import forms
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from basicapp.forms import UserForm,UserProfileInfoForm
from django.contrib.auth.decorators import permission_required


# Create your views here.

def home(request):
	return render(request,'home.html')
	
def index(request):
	return render(request,'basicapp/home.html')
	
def form_name_view(request):
	form=forms.FormName;
	
	if request.method == 'POST':
		form=forms.FormName(request.POST)
		if form.is_valid():
			print("VALIDATION SUCCESS !")
			print("NAME: "+form.cleaned_data['name'])
			print("EMAIL: "+form.cleaned_data['Email'])
			print("TEXT: "+form.cleaned_data['text'])
	
		
	
	
	return render(request,'basicapp/form_page.html',{'form':form})
	
def EmpFormView(request):

	EmpForm=forms.Employee();
	
	if request.method == 'POST':
	
		EmpForm = forms.Employee(request.POST)
		

        if EmpForm.is_valid():
            EmpForm.save(commit=True)
            pemail = request.POST['Email']
            email = EmailMessage('Application Received', 'Thank you for applying to us ! We will verify and get back to you', to=[pemail])
            email.send()
            return home(request)
        else:
            print("ERROR!")
			
	return render(request,'basicapp/EmpForm.html',{'EmpForm':EmpForm})
	
@permission_required('basicapp.create_Model')	
def EditUsers(request):

    Users =	Employee.objects.all();	
		
    return render(request,'basicapp/EditUsers.html',{'UsersList':Users})
	
def DeleteUser(request,id):
    
    dmail=Employee.objects.get(pk=id)

    email = EmailMessage('Your Application is Rejected', 'Thank you for applying to us ! We will verify and get back to you', to=[dmail.Email])
    email.send()
	
    emp=Employee.objects.get(pk=id)
    emp.delete()
	
	
   
    return render(request,'basicapp/EditUsers.html')
	


# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'basicapp/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basicapp/login.html', {})
	return render(request, 'basicapp/login.html', {})
		
@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basicapp/user_login/'
    return HttpResponse("You are logged in. Nice!")
