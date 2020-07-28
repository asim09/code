from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h2>This is my First Django deployment<h2>')


def show(request):
    return HttpResponse('<h2>This is my First Django Show View<h2>')
