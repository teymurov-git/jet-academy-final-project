from django.shortcuts import render
from product.models import ProductCategory
from core.forms import ContactForm

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

def coming_soon(request):
    return render(request, 'coming-soon.html')

def not_found_page(request):
    return render(request, '404.html')