from django.contrib import admin
from django.urls import path
from account.views import signin, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', signin, name = 'signin'),
    path('signup/', signup, name = 'signup')
]
