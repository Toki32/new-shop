from django.shortcuts import render
from test_shop_app.models import Category, Product
# Create your views here.

def base(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'test_shop_app/base.html',context)