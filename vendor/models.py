from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    mobile = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=120,default=None)
