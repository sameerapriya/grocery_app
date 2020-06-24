from django.urls import path
from .views import ProductUpdate, ProductCreate, ProductList
from dashboard.decorators import user_dashboard_permission

app_name = 'product_dashboard'

urlpatterns = [
    path('create/', user_dashboard_permission(ProductCreate.as_view()), name='product_create'),
    path('update/<int:pk>', user_dashboard_permission(ProductUpdate.as_view()), name='product_update'),
    path('list/', user_dashboard_permission(ProductList.as_view()), name='product_list')
]
