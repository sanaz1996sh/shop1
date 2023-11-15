from django.db import models

# Create your models here.
class productcls(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    img=models.ImageField(max_length=100)
    des=models.CharField(max_length=2000)
    category=models.CharField(max_length=50)


class contactcls(models.Model):
    name=models.CharField(max_length=50) 
    subject=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message= models.CharField(max_length=3000)   
                         