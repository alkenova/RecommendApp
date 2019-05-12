from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    description = models.CharField(max_length=400, null=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description":self.description,
            "created_at": self.created_at,
        }


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    product_list = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'description':self.description,
            'product_list':self.product_list
        }