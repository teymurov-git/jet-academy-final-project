from django.contrib import admin
from django.urls import path
from order.views import checkout, empty_cart, cart, wishlist

urlpatterns = [
    path('checkout/', checkout, name = 'checkout'),
    path('emptycart/', empty_cart, name = 'empty_cart'),
    path('cart/', cart, name = 'my_cart'),
    path('wishlist/', wishlist, name = 'wishlist')
]