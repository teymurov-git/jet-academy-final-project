from django.contrib import admin
from django.urls import path
from account.views import signin, signup, profile, logout

urlpatterns = [
    path('signin/', signin, name = 'signin'),
    path('signup/', signup, name = 'signup'),
    path('profile/', profile, name = 'profile'),
    path('logout/', logout, name = 'logout')
]
