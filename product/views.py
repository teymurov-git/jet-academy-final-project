from django.shortcuts import render, get_object_or_404
from product.models import Product, ProductCategory, ProductReview

from django.views.generic import ListView, DetailView


# Create your views here.

class ProductListView(ListView):
    template_name = 'shop-left-sidebar.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        cat_id = self.request.GET.get('category')
        if cat_id:
            queryset = queryset.filter(category = cat_id)
        return queryset
    
# def shop_left_sidebar(request):
#     products = Product.objects.all()
#     categories = ProductCategory.objects.all()
#     context = {
#         'products': products,
#         'categories': categories
#     }
#     return render(request, 'shop-left-sidebar.html', context)

# def product_details(request, pk):
#     try:
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return render(request, '404.html', status=404)

#     context = {
#         'product': product
#     }
#     return render(request, 'product-details.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = ProductReview.objects.filter(product = self.get_object())
        return context



