from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=120,default=None)
    address = models.CharField(max_length=120,default=None)
    email = models.CharField(max_length=120,default=None)
    customer_mobile = models.IntegerField(default=None)

    def __str__(self):
        return self.name

class Cab(models.Model):
    model = models.CharField(max_length=120,default=None)
    number = models.CharField(max_length=120,default=None)
    vendor = models.ForeignKey(Vendor,null=True,on_delete=models.SET_NULL,default=None)


    def __str__(self):
        return self.model