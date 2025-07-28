from rest_framework import serializers
from product.models import ProductCategory, Product


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = [
            'id', 
            'title'
        ]

class ProductSerializer(serializers.ModelSerializer):

    category = serializers.CharField(source = 'category.title')

    class Meta:
        model = Product
        fields = [
            'id', 
            'title',
            'category',
            'price',
            'tags',
            'cover_image',
            'quantity'
        ]