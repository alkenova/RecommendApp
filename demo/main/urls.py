from django.urls import path
from main import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
]