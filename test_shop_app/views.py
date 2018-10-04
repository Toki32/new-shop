from django.shortcuts import render
from test_shop_app.models import Category, Product

# Create your views here.

def index_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'test_shop_app/index.html', context)

def product_view(request, product_slug):
    product= Product.objects.get(slug= product_slug)
    context = {
        'product': product
    }
    return render(request, 'test_shop_app/shop-single.html', context)

def category_view(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug = category_slug)
    product_in_category = Product.objects.filter(category = category)
    context = {
        'categories': categories,
        'category': category,
        'product_in_category': product_in_category
    }
    return render(request, 'test_shop_app/category.html', context)