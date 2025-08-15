from django.db import models
from core.models import AbstractModel
from product.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Basket(AbstractModel):

    user = models.ForeignKey(User, related_name='baskets', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def total_price(self):
        total_price = 0
        for item in self.items.all():
            total_price += item.price()
        return total_price
    
    def total_quantity(self):
        total_quantity = 0
        for item in self.items.all():
            total_quantity += item.quantity
        return total_quantity

    def __str__(self):
        return self.user.username
    

class BasketItem(AbstractModel):

    basket = models.ForeignKey(Basket, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def price(self):
        amount = self.product.price * self.quantity
        return amount

    def __str__(self):
        return self.product.title
    

class Wishlist(AbstractModel):
    user = models.ForeignKey(User, related_name='wishlists', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class WishlistItem(AbstractModel):
    wishlist = models.ForeignKey(Wishlist, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='wishlist_items', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('wishlist', 'product')  # Eyni məhsul iki dəfə əlavə olunmasın

    def __str__(self):
        return self.product.title