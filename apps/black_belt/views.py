from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
import hashlib, sys
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from ..login.models import User
from .models import Item, Wishlist, ItemManager


# Create your views here.
def index(request):
    if 'email' in request.session:
                return redirect('/dashboard')
    else:
        return redirect('/main')
def dashboard(request):
    this_user = User.objects.get(email = request.session['email'])
    context = {
        'user' : this_user,
        'user_wishlist' : Item.objects.filter(wishlist__user = this_user),
        'all_wishlists' : Item.objects.all().exclude(wishlist__user = this_user)
    }
    return render(request, 'black_belt/dashboard.html', context)

def show_item(request, id):
    this_item = Item.objects.get(id = id)
    context = {
        'item' : this_item,
        'all_wishlists': Wishlist.objects.filter(item = this_item)

    }
    return render(request, 'black_belt/item_detail.html', context)

def create(request):
    if request.method == 'GET':
        return render(request, 'black_belt/create.html')
    else:
        if Item.objects.valid(request, request.POST) == True:
            this_user = User.objects.get(email = request.session['email'])
            this_wishlist = Wishlist.objects.get(user = this_user)
            this_item = Item.objects.create(name = request.POST['product'], user = this_user)
            this_item.wishlist.add(this_wishlist)
            return redirect('/dashboard')
        else:
            return redirect('wish_items/create')

def delete(request, id):
    Item.objects.get(id = id).delete()
    return redirect('/dashboard')

def remove(request, id):
    this_user = User.objects.get(email = request.session['email'])
    list = Wishlist.objects.get(user = this_user)
    item = Item.objects.get(id = id)
    item.wishlist.remove(list)
    return redirect('/dashboard')

def add(request, id):
    this_user = User.objects.get(email = request.session['email'])
    this_item = Item.objects.get(id = id)
    this_wishlist = Wishlist.objects.get(user = this_user)
    this_item.wishlist.add(this_wishlist)
    return redirect('/dashboard')
