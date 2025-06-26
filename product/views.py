from django.shortcuts import render, get_object_or_404
from product.models import Product, ProductCategory

# Create your views here.

def shop_left_sidebar(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop-left-sidebar.html', context)

def product_details(request, pk):
    product = get_object_or_404(Product, pk = pk)
    context = {
        'product': product
    }
    return render(request, 'product-details.html', context)
