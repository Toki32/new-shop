from django.contrib import admin
from test_shop_app.models import Category, Brand, Product
# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)