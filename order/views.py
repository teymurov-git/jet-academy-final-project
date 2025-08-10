from django.shortcuts import render, redirect
from order.models import Basket, BasketItem
from django.http import JsonResponse
import json
from product.models import Product

# Create your views here.

def checkout(request):
    return render(request, 'checkout.html')

def empty_cart(request):
    return render(request, 'empty-cart.html')

def cart(request):
    return render(request, 'cart.html')

def wishlist(request):
    return render(request, 'wishlist.html')