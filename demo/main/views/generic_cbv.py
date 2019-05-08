from main.models import Category, Product, Comment
from main.serializers import CategorySerializer, ProductSerializer, CommentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

class products(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class product_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class comment(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        comments = get_object_or_404(Comment, id=self.kwargs.get('pk'))

        queryset = Comment.objects.all()
        body = self.request.query_params.get('text', None)
        if body is not None:
            queryset = queryset.filter(name=text)
        return queryset

class comment_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsAuthenticated,)
