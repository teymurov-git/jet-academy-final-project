from django.shortcuts import render

# Create your views here.

def checkout(request):
    return render(request, 'checkout.html')

def empty_cart(request):
    return render(request, 'empty-cart.html')

def my_cart(request):
    return render(request, 'my-cart.html')

def wishlist(request):
    return render(request, 'wish-list.html')