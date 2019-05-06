from django.urls import path, re_path
from api import views


urlpatterns = [
    path('products/', views.products.as_view()),
    path('products/<int:pk>/', views.product_detail.as_view()),
    path('products/<int:pk>/comments', views.comment.as_view()),
    #path('products/<int:pk>/comments/<int:ik>'. views.comment_detail.as_view())
]

