from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.detail,name='books'),
    path('books/<int:pk>/', views.detail_view, name='detail'),
    path('books/issued/<int:pk>/', views.issue, name='issue'),
    path('issued/',views.issued,name='issued'),

]