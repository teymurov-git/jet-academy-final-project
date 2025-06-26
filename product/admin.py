from django.contrib import admin
from product.models import ProductCategory, Product, ProductImage, ProductReview
# Register your models here.


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'price', 'quantity', 'category']
    list_display_links = ['title']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product']

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']