from django.contrib import admin
from test_shop_app.models import Category, Brand, Product, CartItem, Cart, Shop, Order
# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Shop)
admin.site.register(Order)
