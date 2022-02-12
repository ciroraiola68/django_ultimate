from django.contrib import admin
from .models import Collection, Product, Customer, Order, OrderItem


admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)