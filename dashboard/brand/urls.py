from django.urls import path
from .views import BrandCreate, BrandUpdate, BrandList
from dashboard.decorators import user_dashboard_permission

app_name = 'brand_dashboard'

urlpatterns = [
    path('create/', user_dashboard_permission(BrandCreate.as_view()), name='brand_create'),
    path('update/<int:pk>', user_dashboard_permission(BrandUpdate.as_view()), name='brand_update'),
    path('list/', user_dashboard_permission(BrandUpdate.as_view()), name='brand_list')
]
