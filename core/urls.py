from django.contrib import admin
from django.urls import path
from core.views import homepage, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = 'home'), 
    path('contact/', contact, name = 'contact')
]
