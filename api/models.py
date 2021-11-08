from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# Create your models here.
class Pembeli(models.Model):
    account_id=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.CharField(max_length=254)
    name=models.CharField(max_length=254)
    phone=models.CharField(max_length=16, null=True)
    address=models.CharField(max_length=254,null=True)

    def __str__(self):
        return self.name

class Penjual(models.Model):
    account_id=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.CharField(max_length=254)
    name=models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='product/' )
    price=models.DecimalField(max_digits=9, decimal_places=2)
    penjual_id=models.ForeignKey(Penjual, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Promo(models.Model):
    registered=models.BooleanField()
    penjual_id=models.ForeignKey(Penjual, on_delete=models.CASCADE,related_name='promo')
    
    def __str__(self):
        return self.penjual_id.name

class Notification(models.Model):
    read=models.BooleanField()
    message=models.CharField(max_length=254)
    penjual_id=models.ForeignKey(Penjual,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.message

