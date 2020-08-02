
from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index),
    path('create/', views.create,name='create_vendor'),
    path('cab_create/', views.create_cab,name='create_cab'),
]
