from django.db import models

# Create your models here.

class Cart(models.Model):
    class Meta(object):
    db_table ='cart'

user = models.ForeignKey(
    user, related_name='related_user', on_delete=models.CASCADE
)    
product = models.ForeignKey(
    product, related_name='related_product', on_delete=models.CASCADE    
)
quantity = models.IntegerField (
    'quantity', blank=False, null=False
)

@property
def total_price(self):
    return self.quantity * self.product.price



