from django.contrib import admin
from django.urls import path
from product.views import ProductListView, ProductDetailView

urlpatterns = [
    path('shop_left_sidebar/', ProductListView.as_view(), name = 'shop_left_sidebar'),
    path('shop/<str:slug>', ProductDetailView.as_view(), name = 'product_details'),
]