from django.shortcuts import render
from test_shop_app.models import Category, Product, Cart, CartItem, Shop
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

def index_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    cart = Cart.objects.first()
    context = {
        'categories': categories,
        'products': products,
        'cart': cart
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

def cart_view(request):
    cart= Cart.objects.first()
    context= {
        'cart': cart
    }
    return render(request, 'test_shop_app/cart.html', context)

def add_to_cart_view(request, product_slug):
    product= Product.objects.get(slug= product_slug)
    new_item, _= CartItem.objects.get_or_create(product=product, item_total=product.price)
    cart = Cart.objects.first()
    if new_item not in cart.items.all():
        cart.items.add(new_item, )
        cart.save()

    return HttpResponseRedirect('/cart/')

"""def cart_remove(request, product_id):
    cart = Cart.objects.all()
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')"""

def contact_view(request):
    shops= Shop.objects.all()
    context = {
        'shops': shops
    }
    return render(request, 'test_shop_app/contact.html', context)

def shop_view(request, shop_slug):
    shop= Shop.objects.get(slug= shop_slug)
    context = {
        'shop': shop
    }
    return render(request, 'test_shop_app/store1.html', context)

