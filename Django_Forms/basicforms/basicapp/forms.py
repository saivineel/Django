from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core import validators
from . import models
from basicapp.models import Employee,UserProfileInfo
from django.contrib.auth.models import User

def check_for_z(value):
	if value[0].lower()!='z':
	    raise forms.ValidationError("Name should be starting with z")
		
		
class FormName(forms.Form):
	name=forms.CharField()
	Email=forms.EmailField()
	verify_email=forms.EmailField(label='enter your email again:')
	text=forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(20)])
	

	def clean(self):
		
		email=self.cleaned_data['Email']
		vmail=self.cleaned_data['verify_email']
		
		if email != vmail :
			raise forms.ValidationError('make sure both emails  match')

			
class Employee(forms.ModelForm):

    class Meta():
        model = Employee
        fields = '__all__'
		


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


		
		
		
		
		
		
		


