from django.shortcuts import render, redirect, HttpResponse
from .models import UserManager, User
from django.contrib import messages
import bcrypt
import hashlib, sys
from ..black_belt.models import Wishlist, Item
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    if 'email' in request.session:
        return redirect('/dashboard')
    else:
        return redirect('/main')


def index_page(request):
    return render(request, 'login/index.html')

def register(request):
    if User.objects.valid(request, request.POST) == True:
        salt = bcrypt.gensalt()
        password = request.POST['password']
        User.objects.create(name = request.POST['my_name'], username = request.POST['username'], email = request.POST['email'], password = bcrypt.hashpw(password.encode('utf-8'), salt), date_hired = request.POST['date'])
        print "succes!!!"
        if 'name' in request.session:
            request.session.flush()
        request.session['name'] = request.POST['my_name']
        request.session['username'] = request.POST['username']
        request.session['email'] = request.POST['email']
        context = {
            'method' : 'registering!'
        }
        user = User.objects.get(email = request.session['email'])
        Wishlist.objects.create(user = user)
        return redirect('/dashboard')
    else:
        return redirect('/')


def login(request):
    try:
        email = request.POST['email']
        password = request.POST['password'].encode('utf-8')
        user = User.objects.filter(email = email)
        hashed = user[0].password.encode('utf-8')
        if bcrypt.hashpw(password, hashed) == hashed:
            context = {
                'method' : "logging in!"
            }

            request.session.flush()
            request.session['name'] = user[0].name
            request.session['username'] = user[0].username
            request.session['email'] = user[0].email
            return redirect('/dashboard')
        else:
            messages.add_message(request, messages.INFO, 'invalid username/password', extra_tags = 'login')
            print "heREHEREREEREE"
            return redirect('/')
    except (User.DoesNotExist, ValueError, IndexError):
        messages.add_message(request, messages.INFO, 'invalid username/password', extra_tags = 'login')
        return redirect('/')


def logout(request):
        request.session.flush()
        return redirect('/')
