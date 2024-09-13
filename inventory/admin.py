from django.contrib import admin
from .models import Manufacturer, Warehouse, WarehouseLocation, Item,ItemStock,ItemWarehouseStock

admin.site.register(Manufacturer)
admin.site.register(Warehouse)
admin.site.register(WarehouseLocation)
admin.site.register(Item)
admin.site.register(ItemStock)
admin.site.register(ItemWarehouseStock)