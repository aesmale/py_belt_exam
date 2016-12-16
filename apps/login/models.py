from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re, bcrypt
import hashlib, sys
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect, HttpResponse

password = b"super secret password"

# Create your models here.
class UserManager(models.Manager):
    def valid(self, request, post):
        if len(request.POST['my_name']) < 3:
                messages.add_message(request, messages.INFO, 'Your  name must be longer than 2 characters and may only contain letters', extra_tags = 'register')
                print "somethindsnivndsiovcfisovfijcsviofmvlvjiols"
        elif len(request.POST['username']) < 3:
                messages.add_message(request, messages.INFO, 'Your  username must be longer than 2 characters and may only contain letters', extra_tags = 'register')
                print "somethindsnivndsiovcfisovfijcsviofmvlvjiols"
        elif not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', request.POST['email']):
                messages.add_message(request, messages.INFO, 'invalid email', extra_tags="register")
        elif User.objects.filter(email=request.POST['email']):
                messages.add_message(request, messages.INFO, 'email already exists in database..', extra_tags="register")
        elif len(request.POST['password']) < 8:
                messages.add_message(request, messages.INFO, 'invalid password', extra_tags="register")
        # if len(request.POST['name']) < 3
        # or not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', request.POST['email'])
        # or User.objects.filter(email=request.POST['email']) or len(request.POST['password']) < 8 or len(request.POST['username']) < 3:
        #     print "FAILED VALIDATION!!!!!!!"
        #     return False
        else:
            return True

class User(models.Model):
    name = models.CharField(max_length = 45)
    username = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 100)
    date_hired = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    pass
