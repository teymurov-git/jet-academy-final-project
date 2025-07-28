from rest_framework import serializers
from product.models import ProductCategory, Product
from core.models import Subscriber

class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = [
            'email'
        ]

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

class ProductCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'category',
            'tags',
            'cover_image',
            'quantity',
            'price',
            'slug'
        ]