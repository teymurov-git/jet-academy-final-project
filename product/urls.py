from django.contrib import admin
from django.urls import path
from product.views import product_details, shop_left_sidebar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', shop_left_sidebar, name = 'shop_left_sidebar'),
    path('shopls/', product_details, name = 'product_details')
]