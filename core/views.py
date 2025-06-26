from django.shortcuts import render
from product.models import ProductCategory

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def coming_soon(request):
    return render(request, 'coming-soon.html')

def not_found_page(request):
    return render(request, '404.html')