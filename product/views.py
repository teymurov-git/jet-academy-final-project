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
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return render(request, '404.html', status=404)

    context = {
        'product': product
    }
    return render(request, 'product-details.html', context)