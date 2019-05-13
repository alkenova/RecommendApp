from main.models import Category, Comment
from main.serializers import CategorySerializer,CategorySerializer2, CommentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer2

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

