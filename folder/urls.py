from django.contrib import admin
from django.urls import path,include
from folder import views

urlpatterns = [
   
    path('',views.index,name='home'),
    path('login.html',views.index,name='login'),
    path('index.html',views.index,name='index'),
    path('register', views.register, name='register'),
    path('login', views.userlogin, name='userlogin'),
    path('logout', views.userlogout, name='userlogout'),
    path('index', views.index, name='index'),
    path('confirm', views.confirm, name='confirm'),
]
