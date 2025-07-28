from django.http import JsonResponse
from product.models import ProductCategory, Product
from core.models import Subscriber
from product.api.serializers import (ProductCategorySerializer,
                                    ProductSerializer,
                                    ProductCreateSerializer,
                                    SubscriberSerializer)
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView


class SubscriberCreateAPIView(CreateAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()

@api_view(http_method_names=['GET', 'POST'])
def categories(request):
    if request.method == 'POST':
        serializer_class = ProductCategorySerializer(data = request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(data=serializer_class.data, safe=False)
        return JsonResponse(data=serializer_class.errors, safe=False)
    category_list = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer(category_list, many = True)
    # category_dict = []
    # for category in category_list:
    #     if category.parent:
    #         category_dict.append({
    #                 'parent': category.parent.id,
    #                 'id': category.id,
    #                 'title': category.title
    #             })
    #     else:
    #         category_dict.append({
    #                 'id': category.id,
    #                 'title': category.title
    #             })
    return JsonResponse(data = serializer_class.data, safe=False)

class ProductAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            serializer_class = ProductCreateSerializer
            return serializer_class
        return self.serializer_class

# @api_view(http_method_names = ['GET', 'POST'])
# def products(request):
#     if request.method == 'POST':
#         serializer_class = ProductCreateSerializer(data=request.data, context={'request': request})
#         if serializer_class.is_valid():
#             serializer_class.save()
#             return JsonResponse(data=serializer_class.data, safe=False, status = 201) 
#         return JsonResponse(data=serializer_class.errors, safe=False, status = 400)
#     product_list = Product.objects.all()
#     serializer_class = ProductSerializer(product_list, context={'request': request}, many=True)
#     return JsonResponse(data = serializer_class.data, safe=False, status = 200)
    
class ProductUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCreateSerializer 
    queryset = Product.objects.all()

@api_view(http_method_names = ['PUT', 'PATCH'])
def product_update(request, pk):
    if request.method == 'PUT':
        product = Product.objects.get(id = pk)
        serializer_class = ProductSerializer(product, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(data=serializer_class.data, safe=False) 
        return JsonResponse(data=serializer_class.errors, safe=False)
    if request.method == 'PATCH':
        product = Product.objects.get(id = pk)
        serializer_class = ProductSerializer(product, data=request.data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(data=serializer_class.data, safe=False) 
        return JsonResponse(data=serializer_class.errors, safe=False)
    product_list = Product.objects.all()
    serializer_class = ProductSerializer(product_list, context={'request': request}, many=True)
    return JsonResponse(data = serializer_class.data, safe=False)