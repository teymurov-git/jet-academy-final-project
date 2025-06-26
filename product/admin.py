from django.contrib import admin
from django.contrib.admin import TabularInline
from product.models import ProductCategory, Product, ProductImage, ProductReview, ProductTag
# Register your models here.

class ProductImageInLine(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'price', 'quantity', 'category', 'get_tags']
    list_display_links = ['title']
    list_editable = ['category']
    list_filter = ['category', 'price', 'tags']
    search_fields = ['title', 'category__title']
    list_per_page = 10
    inlines = [ProductImageInLine]

    def get_tags(self, obj):
        tags = []
        for tag in obj.tags.all():
            tags.append(tag.title)
        return tags

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']

# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ['product']

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']

@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['title']