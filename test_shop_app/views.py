
from test_shop_app.models import Category, Product, Cart, CartItem, Shop, Order
from django.http import HttpResponseRedirect
from django.shortcuts import render
from test_shop_app.forms import OrderForm, LoginForm, RegistrationForm
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import get_template
from django.contrib.auth import login, authenticate


# Create your views here.

def index_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'cart': cart

    }
    return render(request, 'test_shop_app/index.html', context)

def product_view(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)

    product= Product.objects.get(slug= product_slug)
    context = {
        'product': product,
        'cart': cart
    }
    return render(request, 'test_shop_app/shop-single.html', context)

def category_view(request, category_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()
    category = Category.objects.get(slug = category_slug)
    product_in_category = Product.objects.filter(category = category)
    context = {
        'cart': cart,
        'categories': categories,
        'category': category,
        'product_in_category': product_in_category
    }
    return render(request, 'test_shop_app/category.html', context)

def cart_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context= {
        'cart': cart
    }
    return render(request, 'test_shop_app/cart.html', context)

def add_to_cart_view(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product= Product.objects.get(slug= product_slug)
    new_item, _= CartItem.objects.get_or_create(product=product, item_total=product.price)
    if new_item not in cart.items.all():
        cart.items.add(new_item)
        cart.save()
        return HttpResponseRedirect('/cart/')

def remove_from_cart_view(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product= Product.objects.get(slug= product_slug)
    for cart_item in cart.items.all():
        if cart_item.product == product:
            cart.items.remove(cart_item)
            cart.save()
            return HttpResponseRedirect('/cart/')



    return HttpResponseRedirect('/cart/')

def contact_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    shops= Shop.objects.all()
    context = {
        'cart': cart,
        'shops': shops
    }
    return render(request, 'test_shop_app/contact.html', context)

def shop_view(request, shop_slug):
    shop= Shop.objects.get(slug= shop_slug)
    context = {
        'shop': shop
    }
    return render(request, 'test_shop_app/store1.html', context)

def checkout_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    form = OrderForm(request.POST or None)
    context = {
            'form': form,
            'cart': cart
        }
    return render(request, 'test_shop_app/checkout.html', context)




#Отправка писем





def success(request, usermail):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    htmly= get_template('test_shop_app/letter.html')
    context = {
        'cart': cart,
        }
    data= htmly.render(context)

    send_mail('Welcome!', data, "kekvald@yandex.ru",
                  [usermail], fail_silently=False)
    return render(request, 'test_shop_app/thankyou.html')


def make_order_view(request):

    form = OrderForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']
        phone = form.cleaned_data['phone']
        address = form.cleaned_data['address']
        comments = form.cleaned_data['comments']
        email= form.cleaned_data['email']

        new_order = Order()
        new_order.user= request.user
        new_order.save()
        new_order.first_name = name
        new_order.last_name = last_name
        new_order.phone = phone
        new_order.address = address
        new_order.comments = comments
        new_order.email = email
        new_order.save()
        emailsend = success(request, new_order.email)

        del request.session['cart_id']
        return emailsend
    return render(request, 'test_shop_app/checkout.html')

def account_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context = {
        'cart': cart
    }

    return render(request, 'test_shop_app/account.html', context)

def registration_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        new_user.username = username
        new_user.set_password(password)
        new_user.email = email
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('index'))
    context = {
        'form': form,
        'cart': cart,
    }
    return render(request, 'test_shop_app/registration.html', context)




def login_view(request):

    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('index'))
    context = {
        'form': form,

    }
    return render(request, 'test_shop_app/login.html', context)

