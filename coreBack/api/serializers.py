from rest_framework import serializers
from .models import Product, Comment

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=True)
    comments = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'created_at', 'comments')

class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'created_at', 'product_id')
