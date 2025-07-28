from product.api.views import categories, products
from django.urls import path

urlpatterns = [
    path('categories/', categories, name='categories'),
    path('products/', products, name='products')
]