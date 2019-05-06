from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProductManager(models.Manager):
    def for_user(self, user):
        self.filter(created_by = user).order_by('name')


class Product(models.Model):
    name = models.CharField(max_length = 200)
    created_at = models.DateTimeField()

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Comment(models.Model):
    text = models.TextField(),
    created_at = models.DateTimeField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    def __str__(self):
        return '{}: {}'.format(self.id, self.product_id)

    def to_json(self):
        return {
            'id': self.id,
            'comment': self.text,
            'created at': self.created_at
        }