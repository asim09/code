from django.shortcuts import render,HttpResponse,redirect
from .forms import VendorForm,CabForm
from .models import Vendor,Cab

# Create your views here.

def index(request):
    return render(request,'vendor/dashboard.html')


def create(request):
    form = VendorForm()
    data = Vendor.objects.all()
    
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'vendor/create.html',context)





def create_cab(request):
    form = CabForm()
    # data = Cab.objects.all()
    
    if request.method == 'POST':
        form = CabForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'vendor/cab_create.html',context)


    