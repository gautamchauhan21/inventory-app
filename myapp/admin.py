from django.contrib import admin
from .models import Inventory

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id','inventory_name','price','stocks_left')

admin.site.register(Inventory,InventoryAdmin)
