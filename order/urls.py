from django.contrib import admin
from django.urls import path
from order.views import checkout, empty_cart, my_cart, wishlist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkout/', checkout, name = 'checkout'),
    path('emptycart/', empty_cart, name = 'empty_cart'),
    path('mycart/', my_cart, name = 'my_cart'),
    path('wishlist/', wishlist, name = 'wishlist')
]