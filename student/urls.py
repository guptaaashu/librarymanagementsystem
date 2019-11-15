from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^students/login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    path('',views.first,name='first'),
]
