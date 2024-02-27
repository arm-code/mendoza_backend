from django.contrib import admin
from .models import Forniture, FornitureCategory,FornitureCombos, Product, ShoppingCart,PurchaseOrder, DetailedOrder, Address, Client

# Register your models here.
admin.site.register(Forniture)
admin.site.register(FornitureCategory)
admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(PurchaseOrder)
admin.site.register(FornitureCombos)
admin.site.register(DetailedOrder)
admin.site.register(Address)
admin.site.register(Client)
