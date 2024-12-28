from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Cart(models.Model):
    user_id=models.ForeignKey(User, related_name=("user_carts"), on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product, related_name=("product_carts"), on_delete=models.CASCADE)
    quantity= models.IntegerField()
