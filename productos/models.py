from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.contrib.auth.models import User

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    creation_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
class ProductsReferences(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=5)
    product = models.ForeignKey(Products, on_delete=models.PROTECT)
    
class PlatformUser(User):
    identity_card = models.CharField(max_length=20)    
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    