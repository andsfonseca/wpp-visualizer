from django import urls
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_r, name='index'),
    path('isConnected', views.isConnected, name='index'),
    path('qr', views.qr, name='index'),
]