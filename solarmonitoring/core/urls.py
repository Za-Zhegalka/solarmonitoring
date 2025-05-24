from django.urls import path
from . import views

urlpatterns = [
    # Админские URLs
    path('base/', views.base, name='base'),
    path('base/profile/', views.admin_profile, name='admin_profile'),
    path('base/dashboard/users/', views.admin_user_list, name='admin_user_list'),
    path('base/dashboard/support/', views.admin_support_requests, name='admin_support'),
    path('base/dashboard/analytics/', views.admin_action_analytics, name='admin_analytics'),
    path('base/dashboard/moderation/', views.admin_sales_moderation, name='admin_moderation'),
    path('base/community/', views.admin_community, name='admin_community'),
    path('base/map/', views.admin_interactive_map, name='admin_map'),
    path('base/sales/', views.admin_sales_board, name='admin_sales'),
]