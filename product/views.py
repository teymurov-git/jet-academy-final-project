from django.shortcuts import render
from product.models import Product, ProductCategory

# Create your views here.

def shop_left_sidebar(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop-left-sidebar.html', context)

def product_details(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'product-details.html', context)
