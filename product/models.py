from django.db import models
from core.models import AbstractModel

# Create your models here.

class ProductCategory(AbstractModel):

    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField('title',max_length=100)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.title}'
        return f'{self.title}'
    
    class Meta:
        """ bu setir bize admin panelde duzgun cemlendirme yazilisina komek edir. """
        verbose_name_plural = 'Product Categories' 

class Product(AbstractModel):

    category = models.ForeignKey(ProductCategory, related_name='products', on_delete=models.CASCADE)

    title = models.CharField('title', max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    decription = models.TextField('description')
    cover_image = models.ImageField('cover_image', upload_to='product_images/')
    quantity = models.IntegerField('quantity', default=1)

    def __str__(self):
        return f'{self.title}'
    
class ProductImage(AbstractModel):

    image = models.ImageField('image', upload_to='product_images/')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title
    
    class Meta:
        verbose_name_plural = 'Product Images'