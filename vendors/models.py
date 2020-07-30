from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=20,null=False)
    mobile = models.IntegerField()
    email = models.CharField(max_length=50,null=False)
    addres = models.TextField(null=True,blank=True )

    def __str__(self):
        return self.name
