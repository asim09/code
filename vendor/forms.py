from django import forms
from django.forms import ModelForm
from .models import Vendor,Cab

def get_vendor_data():
    data = Vendor.objects.values('name')
    print(data)
    return data


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

class CabForm(ModelForm):
    class Meta:
        model = Cab
        # fields = ['model','number']
        fields = '__all__'
        vendor_name = get_vendor_data()
        widgets = {
            'age': forms.Select(choices=vendor_name,attrs={'class': 'form-control'}),
        }

