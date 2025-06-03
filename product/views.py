from django.shortcuts import render

# Create your views here.

def product_details(request):
    return render(request, 'product-details.html')

def shop_left_sidebar(request):
    return render(request, 'shop-left-sidebar.html')