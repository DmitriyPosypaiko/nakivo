from django.db import models
from django.contrib.auth.models import User

from django.utils.safestring import mark_safe


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    def image_tag(self):
        return mark_safe('<img src="../../../media/%s" width="60" height="60" />' % (self.image))

    image_tag.short_description = 'Image'
