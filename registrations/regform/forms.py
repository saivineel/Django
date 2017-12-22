from django import forms

from .models import Application

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = (
		'FirstName',
		'MiddleName',
		'LastName',
		'MobileNumber',
		'EmailId',
		'Country')

