from django.db import models

# Create your models here.
class Cart(models.Model):
    username = models.CharField(max_length=100)
    product_id = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=5)
    ### It will help to print the values.
    def __str__(self):
        return '%s %s %s %s ' % (self.username, self.product_id, self.price, self.quantity)
