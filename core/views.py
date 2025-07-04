from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from product.models import ProductCategory
from core.forms import ContactForm

from django.views.generic import CreateView


# Create your views here.

def homepage(request):
    return render(request, 'index.html')

class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        messages.success(self.request, 'Messages has sent to succesfull!')
        return super().form_valid(form)


# def contact(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(data = request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Messages has sent to succesfull!')
#         return redirect(reverse_lazy('contact'))
#     context = {
#         'form': form
#     }
#     return render(request, 'contact.html', context)

def coming_soon(request):
    return render(request, 'coming-soon.html')

def not_found_page(request):
    return render(request, '404.html')