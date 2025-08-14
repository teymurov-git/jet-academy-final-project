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
    basket = Basket.objects.filter(user = request.user, is_active = True).first()
    context = {
        'basket': basket,
    }
    return render(request, 'cart.html', context)

def wishlist(request):
    return render(request, 'wishlist.html')

def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    product = Product.objects.get(id = productId)

    basket, created = Basket.objects.get_or_create(user = request.user, is_active = True)
    basketItem, created = BasketItem.objects.get_or_create(basket = basket, product = product)

    if action == 'add':
        if not created:
            basketItem.quantity += 1
    if action == 'remove':
        basketItem.quantity -= 1

    basketItem.save()

    if basketItem.quantity <= 0:
        basketItem.delete()

    return JsonResponse('Item was added!', safe=False)