from django.http import JsonResponse
from product.models import ProductCategory, Product
from product.api.serializers import ProductCategorySerializer, ProductSerializer


def categories(request):
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

def products(request):
    category_list = Product.objects.all()
    context = {
        'request': request
        }
    serializer_class = ProductSerializer(category_list, many = True)

    return JsonResponse(data = serializer_class.data, safe=False)