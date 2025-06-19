from django.db import models

# Create your models here.

class AbstractModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Contact(AbstractModel):

    first_name = models.CharField('first_name', max_length=200)
    last_name = models.CharField('last_name', max_length=200)
    phone = models.CharField('phone', null=True, blank=True)
    email = models.EmailField('email', max_length=100)
    message = models.TextField('message')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Subscriber(AbstractModel):
    
    email = models.EmailField('email', max_length=200)

    def __str__(self):
        return self.email