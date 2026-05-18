from django.contrib import admin

# Register your models here.
from .models import MenuItem, Table, Reservation, Order, OrderItem, InventoryItem

admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(InventoryItem)