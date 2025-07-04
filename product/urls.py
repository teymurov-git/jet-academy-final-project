from django.contrib import admin
from django.urls import path
from product.views import product_details, ProductListView

urlpatterns = [
    path('shop_left_sidebar/', ProductListView.as_view(), name = 'shop_left_sidebar'),
    path('shop/<int:pk>', product_details, name = 'product_details')
]