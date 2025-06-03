from django.contrib import admin
from django.urls import path
from blog.views import blog, blog_details

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', blog, name = 'blog'),
    path('details/', blog_details, name = 'blog_details')
]