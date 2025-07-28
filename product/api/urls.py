from product.api.views import categories, ProductAPIView, ProductUpdateDeleteAPIView, SubscriberCreateAPIView
from django.urls import path

urlpatterns = [
    path('categories/', categories, name='categories'),
    path('products/', ProductAPIView.as_view(), name='products'),
    path('subscriber/', SubscriberCreateAPIView.as_view(), name='subcriber'),
    path('products/<int:pk>', ProductUpdateDeleteAPIView.as_view(), name='product')
]