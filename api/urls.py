from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns=[
    path('penjual/', PenjualView.as_view(), name='penjual'),
    path('daftar/account/', DaftarAccount.as_view(), name="daftar_account"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#login
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),#refresh login
    path('daftar/penjual/', DaftarPenjual.as_view(), name="daftar_penjual"),
    path('seller/',LoginSeller.as_view(),name='seller'),
    path('daftar/product/',DaftarProduct.as_view(),name='daftar_product'),
    path('daftar/promo/',DaftarPromo.as_view(),name='daftar_promo'),

]