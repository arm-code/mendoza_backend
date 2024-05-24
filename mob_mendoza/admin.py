from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Forniture)
admin.site.register(FornitureCategory)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Component)



