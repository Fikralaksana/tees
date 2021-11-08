from django.contrib import admin
from .models import Penjual,Pembeli,Product,Promo,Notification

# Register your models here.

admin.site.register(Penjual)
admin.site.register(Pembeli)
admin.site.register(Product)
admin.site.register(Promo)
admin.site.register(Notification)
