# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django.core.urlresolvers import reverse

# Create your models here.

class Application(models.Model):
    FirstName=models.CharField(max_length=20);
    MiddleName=models.CharField(max_length=20);
    LastName=models.CharField(max_length=20);
    MobileNumber=models.IntegerField();
    EmailId=models.EmailField();
    Country=models.CharField(max_length=20);

    def get_absolute_url(self):
        return reverse()

    def __str__(self):
        return self.FirstName


		
