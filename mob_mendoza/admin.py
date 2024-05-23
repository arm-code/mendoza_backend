from django.contrib import admin
from .models import Forniture, FornitureCategory,FornitureCombos, Product

# Register your models here.
admin.site.register(Forniture)
admin.site.register(FornitureCategory)
admin.site.register(Product)
admin.site.register(FornitureCombos)
