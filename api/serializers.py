from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import Penjual,Pembeli,Product,Promo,Notification
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ErrorMessages(serializers.Serializer):
    detail=serializers.CharField(max_length=999999)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']

class PembeliSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pembeli
        fields=['name','email','account_id']

class PenjualSerializer(serializers.ModelSerializer):
    class Meta:
        model=Penjual
        fields=['name','email','account_id']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['name','image','price','penjual_id']

class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Promo
        fields=['registered','penjual_id']