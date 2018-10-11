"""test_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


urlpatterns = [
    path('', views.index_view, name='index'),
    re_path(r'^product/(?P<product_slug>[-\w]+)/$', views.product_view, name= 'product_kek'),
    re_path(r'^category/(?P<category_slug>[-\w]+)/$', views.category_view, name= 'category_kek'),
    re_path(r'^add_to_cart/(?P<product_slug>[-\w]+)/$', views.add_to_cart_view, name= 'add_to_cart'),
    re_path(r'^remove/(?P<product_slug>[-\w]+)/$', views.remove_from_cart_view, name= 'remove_from_cart'),
    re_path(r'^cart/$', views.cart_view, name= 'cart'),
    re_path('contact/', views.contact_view, name= 'contact'),
    re_path(r'^shop/(?P<shop_slug>[-\w]+)/$', views.shop_view, name= 'shop'),
    re_path('checkout/', views.checkout_view, name= 'checkout'),
    re_path('success/', views.success, name= 'thankyou'),
    re_path(r'^make_order/$', views.make_order_view, name='make_order'),
    re_path(r'^registration/$', views.registration_view, name='registration'),
    re_path(r'^login/$', views.login_view, name='login'),
    re_path(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
    re_path(r'^account/$', views.account_view, name='account'),


]