from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(AbstractUser):
    photo = models.ImageField('photo', upload_to='user_photos/' ,null=True, blank=True)
    phone = models.CharField('phone', max_length=100, null=True, blank=True)
    bio = models.TextField('bio', null=True, blank=True)
    ips = ArrayField(models.GenericIPAddressField(), null=True, blank=True)
    email = models.EmailField("email address", unique=True)\
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = '',

    def __str__(self):
        return self.username

class BlockIpAdress(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address