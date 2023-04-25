from django.contrib import admin
from order.models import *
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone","address")
    search_fields = ("name","phone")
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "section", "price")
    search_fields = ("name", "section")
    list_filter = ("section",)

class OrderAdmin(admin.ModelAdmin):
    list_display = ("number", "date", "is_delivered")
    search_fields = ("number",)
    list_filter = ("date",)
    date_hierarchy = "date"

admin.site.register(Client, ClientAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)

