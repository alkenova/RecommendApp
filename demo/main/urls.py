from django.urls import path
from main import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('products/', views.products.as_view()),
    path('products/<int:pk>/', views.product_detail.as_view()),
    path('products/<int:pk>/comments', views.comment.as_view()),
]