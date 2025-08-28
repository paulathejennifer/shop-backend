from django.db import models

from decimal import Decimal


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 28)
 
class Tag(models.Model):
    name = models.CharField(max_length = 28)

     
class User(models.Model):
    name = models.CharField(max_length = 28)

class Membership(models.Model):
    user =models.ForeignKey(User, on_delete = models.PROTECT)

class Product(models.Model):
    name = models.CharField(max_length=50, default ="")
    stock = models.IntegerField(default = 0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    description = models.TextField(default="") 
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT, blank=True, default="")

    def __str__(self):
        return self.name



class Farmer (models.Model):
    membership = models.OneToOneField(Membership, on_delete=models.PROTECT)
   


    
