from django.contrib import admin

# Register your models here.
from order.models import Product,Ptype,Order,UserProfile

admin.site.register(Product)
admin.site.register(Ptype)
admin.site.register(Order)
admin.site.register(UserProfile)