from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets,views
from rest_framework import permissions,status
from rest_framework.response import Response
from .models import Penjual,Pembeli,Product,Notification
from .serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer

from rest_framework.permissions import IsAuthenticated
from .access import IsPenjual
import io
from rest_framework.parsers import JSONParser

# Create your views here.
class PenjualView(views.APIView):
    
    def get(self,request,format=None):
        produk=Product.objects.all()
        produk=ProductSerializer(produk,many=True)        
        return Response(produk.data)


class DaftarAccount(views.APIView):
    def post(self,request):
        dataAkun=request.POST.copy()
        dataPembeli=dataAkun
        dataPembeli['name']=dataAkun.get('username')
        dataPembeli['account_id']=1
        daftarAkun=UserSerializer(data=dataAkun)
        daftarPembeli=PembeliSerializer(data=dataPembeli)
        try:
            if daftarAkun.is_valid():
                daftarAkun.validated_data['password']=make_password(daftarAkun.validated_data.get('password'))
                user=daftarAkun.save()
            else :
                return Response(daftarAkun.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
            if daftarPembeli.is_valid():
                daftarPembeli.validated_data['account_id']=user
                daftarPembeli.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response({'detail':'user created, BUT'+daftarPembeli.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response(str(e),status=status.HTTP_406_NOT_ACCEPTABLE)


class DaftarPenjual(views.APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        user=request.user
        data={}
        data['email']=user.email
        data['name']=user.username
        data['account_id']=user.id
        penjual=PenjualSerializer(data=data)
        try:
            if penjual.is_valid():
                penjual.save()
                print(penjual.validated_data)
                return Response(status=status.HTTP_201_CREATED)
            else :
                return Response(penjual.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response(str(e),status=status.HTTP_406_NOT_ACCEPTABLE)

class LoginSeller(views.APIView):
    permissions_classes= [IsAuthenticated]
    def post(self,request):
        try:
            user=request.user.penjual
            penjual=PenjualSerializer(user)
            data=penjual.data
            try:
                promo=user.promo.get(penjual_id=user).registered
                return Response(data,status=status.HTTP_200_OK)
            except Exception as e:
                data['messages']="anda belum terdaftar di promo"
                return Response(data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail':'not registered as a seller'},status=status.HTTP_401_UNAUTHORIZED)
 

class DaftarProduct(views.APIView):
    permission_classes = [IsPenjual]
    def post(self,request):
        try:
            data=request.POST.copy()
            user=request.user
            image=request.FILES.get('image')
            data['image']=image
            data['penjual_id']=user.penjual.id
            product=ProductSerializer(data=data)
            if product.is_valid():
                product.save()
                try:
                    promo=user.promo.get(penjual_id=user).registered
                    return Response(data,status=status.HTTP_200_OK)
                except Exception as e:
                    data={}
                    data['messages']="anda belum terdaftar di promo"
                    return Response(data,status=status.HTTP_200_OK)
            else:
                return Response(product.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            em={'detail':'not registered as a seller'}
            error=ErrorMessages(data=em)
            error.is_valid()
            return Response(error.data,status=status.HTTP_401_UNAUTHORIZED)

class DaftarPromo(views.APIView):
    permission_classes = [IsPenjual]
    def post(self,request):
        try:
            user=request.user
            data={}
            data['registered']=True
            data['penjual_id']=user.penjual.id
            promo=PromoSerializer(data=data)
            if promo.is_valid():
                promo.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(promo.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            em={'detail':'not registered as a seller'}
            error=ErrorMessages(data=em)
            error.is_valid()
            return Response(error.data,status=status.HTTP_401_UNAUTHORIZED)






        

