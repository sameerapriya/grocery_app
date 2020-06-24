from django.urls import path
from .views import ProductDetail, ProductList

app_name = 'products'

urlpatterns = [
    path('<str:slug>', ProductDetail.as_view(), name='product_detail'),
    path('category/<str:slug>', ProductList.as_view(), name='product_list'),
]
