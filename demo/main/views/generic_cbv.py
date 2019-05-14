from main.models import Category, Comment, Product
from main.serializers import CategorySerializer,CategorySerializer2, CommentSerializer, ProductSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import Http404

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer2


class CommentList(generics.ListCreateAPIView):

    serializer_class = CommentSerializer
    
    def get_queryset(self):
        try:
            product = Product.objects.get(id=self.kwargs['pk'])
        except:
            raise Http404

        return Comment.objects.product_filter(product=product)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    filter_backends = ()