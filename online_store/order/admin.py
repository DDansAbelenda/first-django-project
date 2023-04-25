from django.contrib import admin
from order.models import *
# Register your models here.

admin.site.register(Client)
admin.site.register(Item)
admin.site.register(Order)

