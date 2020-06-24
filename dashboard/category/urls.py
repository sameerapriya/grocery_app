from django.urls import path
from .views import CreateCategory, UpdateCategory, ListCategory, CreateSubCategory, category_tree
from dashboard.decorators import user_dashboard_permission

app_name = 'category_dashboard'

urlpatterns = [
    path('create/', user_dashboard_permission(CreateCategory.as_view()), name='category_create'),
    path('create/<int:pk>', user_dashboard_permission(CreateSubCategory.as_view()), name='sub_category_create'),
    path('update/<int:pk>', user_dashboard_permission(UpdateCategory.as_view()), name='category_update'),
    path('list/', user_dashboard_permission(ListCategory.as_view()), name='category_list'),
    path('<int:pk>/', user_dashboard_permission(category_tree), name='category_detail')
]
