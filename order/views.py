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

from django.shortcuts import redirect
from product.models import Product
from .models import Basket, BasketItem

def add_to_basket(request, product_id):
    product = Product.objects.get(id=product_id)
    basket, created = Basket.objects.get_or_create(user=request.user, is_active=True)
    basket_item, created = BasketItem.objects.get_or_create(basket=basket, product=product)
    basket_item.quantity += int(request.POST.get('quantity', 1))
    basket_item.save()
    return redirect('my_cart')  # Cart səhifəsinə yönləndirmək


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    product = Product.objects.get(id=productId)

    basket, created = Basket.objects.get_or_create(user=request.user, is_active=True)
    basketItem, created = BasketItem.objects.get_or_create(basket=basket, product=product)

    if action == 'add':
        # hər klikdə quantity 1 olaraq qalır
        basketItem.quantity = 1
        basketItem.save()

    elif action == 'remove':
        basketItem.delete()  # tamamilə silinir

    return JsonResponse('Item was updated!', safe=False)
