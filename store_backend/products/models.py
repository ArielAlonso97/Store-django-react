from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50,null=False)
    desciption = models.TextField(max_length=500,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/assets/', blank=True, null=True)
