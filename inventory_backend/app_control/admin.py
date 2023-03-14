from django.contrib import admin
from .models import InventoryGroup, Inventory

# Register your models here.

admin.site.register((InventoryGroup, Inventory, ))
