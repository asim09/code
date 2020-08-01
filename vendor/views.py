from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'vendor/dashboard.html')

def show(request):
    return render(request,'vendor/show.html')
