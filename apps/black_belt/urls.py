from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'dashboard$', views.dashboard),
    url(r'wish_items/(?P<id>\d+)$', views.show_item),
    url(r'wish_items/create$', views.create),
    # url(r'wish_items/add$', views.create),
    url(r'delete/(?P<id>\d+)$', views.delete),
    url(r'remove/(?P<id>\d+)$', views.remove),
    url(r'add/(?P<id>\d+)$', views.add)

]
