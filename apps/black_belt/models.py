from __future__ import unicode_literals
from django.db import models
from ..login.models import User
from django.contrib import messages



# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class ItemManager(models.Manager):
    def valid(self, request, item):
        if len(request.POST['product']) < 1:
            messages.add_message(request, messages.INFO, 'This field cannot be blank')
        elif len(request.POST['product']) < 3:
            messages.add_message(request, messages.INFO, 'Your  product should be longer than 3 characters')
        else:
            return True
        if len(request.POST['product']) < 3:
            return False


class Item(models.Model):
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    wishlist = models.ManyToManyField(Wishlist)
    objects = ItemManager()
    pass
