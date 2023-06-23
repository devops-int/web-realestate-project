from django.db import models

from django.contrib.auth.models import User 
# Create your models here.

class Catergory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = 'Currency'

    def __str__(self):
        return self.name
 
class Item(models.Model):
    catergory_id = models.ForeignKey(Catergory, related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    descripion = models.TextField(blank=True, null=True)
    price = models.FloatField()
    currency_value = models.ForeignKey(Currency, related_name='items',on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, null=True)
    contact_info = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='items',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

