from django.db import models

# Create your models here.

class Comment(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    product_id = models.CharField(max_length=10)
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    comment = models.TextField()
    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.fname, self.lname, self.email, self.mobile, 
                self.address, self.product_id, self.product_name, self.price, self.comment)
    

