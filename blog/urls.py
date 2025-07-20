from django.urls import path
from blog.views import BlogListView, BlogDetailView

urlpatterns = [
    path('blog', BlogListView.as_view(), name='blog'),
    path('blog-details/<int:pk>/', BlogDetailView.as_view(), name='blog_details'),
]