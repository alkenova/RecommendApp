from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import Category, Product


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    def create(self, validated_data):
        category = Category(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class CategorySerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)
    description = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'created_by',)
        # fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=True)
    image = serializers.CharField(read_only=True)
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(read_only=True)
    product_list = CategorySerializer(required=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image', 'created_at', 'product_list')
