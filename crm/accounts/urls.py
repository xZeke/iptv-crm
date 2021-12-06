from django import urls
from django.urls import path, include

from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('new_customer/', views.createCustomer, name="new_customer"),
    path('update_customer/<str:pk>/', views.updateCustomer, name="update_customer"),
    path('delete_customer/<str:pk>/', views.deleteCustomer, name="delete_customer"),
    path('remind_customer/', views.remindCustomer, name="remind_customer")
]
