from product.models import ProductCategory
from django.template import Library
register = Library()

@register.simple_tag()
def get_categories():
    return ProductCategory.objects.filter(parent = None)