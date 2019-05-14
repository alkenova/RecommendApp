from django.contrib import admin
from django.urls import path
from auth_ import views

urlpatterns = [
    path('users/', views.UserList.as_view())
]
