from django.db import models
from mptt.models import MPTTModel
from mptt.managers import TreeManager
from django.urls import reverse_lazy


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(upload_to='category_background_images', blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    tree = TreeManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('dashboard:category_dashboard:category_list')


class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    image = models.ImageField()

    def get_absolute_url(self):
        return reverse_lazy('dashboard:brand_dashboard:brand_list')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    weight = models.FloatField()
    sku = models.CharField(max_length=30, unique=True)
    stock = models.PositiveIntegerField()
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('dashboard:product_dashboard:product_list')


class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    alt = models.CharField(max_length=255)


