from django.contrib import admin
from django.urls import path
from core.views import homepage, contact, coming_soon, not_found_page

urlpatterns = [
    path('', homepage, name = 'home'), 
    path('contact/', contact, name = 'contact'),
    path('soonex/', coming_soon, name = 'coming_soon'),
    path('404/', not_found_page, name = 'not_found_page')
]
