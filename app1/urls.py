from django.urls import path
from . import views



urlpatterns =[
    path('',views.index),
    path('product',views.product),
    path('orders',views.orders),
    path('customers',views.customers),
    path('sales',views.sales),
]