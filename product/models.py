from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    category_name = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ["name"]
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey('Category', on_delete=models.SET, null=True, blank=True)


    def __str__(self):
        return self.name

