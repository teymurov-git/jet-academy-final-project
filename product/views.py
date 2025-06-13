from django.shortcuts import render
from product.models import Product

# Create your views here.

def product_details(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product-details.html', context)

def shop_left_sidebar(request):
    return render(request, 'shop-left-sidebar.html')