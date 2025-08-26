from symtable import Class

from django.db import models
from django.db.models import IntegerField
from django.forms import BooleanField


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    web_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    size = models.CharField(max_length=1000)
    is_available = BooleanField()
    rating = IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    brand_id = models.ForeignKey(Brand,on_delete=models.CASCADE)
    cate_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=1000)
    msg = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
