from django.shortcuts import render,HttpResponse
import os

# Create your views here.

def index(request):
    print(os.getcwd())
    return HttpResponse('<h2>This is my First Django deployment<h2>')


def show(request):
    return HttpResponse('<h2>This is my First Django Show View<h2>')
