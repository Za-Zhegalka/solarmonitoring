from django.urls import path
from . import admin_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('dashboard/', login_required(admin_views.dashboard), name='admin_dashboard'),
    path('profile/', login_required(admin_views.profile), name='admin_profile'),
    path('dashboard/users/', login_required(admin_views.user_list), name='admin_user_list'),
    path('dashboard/support/', login_required(admin_views.support_requests), name='admin_support'),
    path('dashboard/analytics/', login_required(admin_views.action_analytics), name='admin_analytics'),
    path('dashboard/moderation/', login_required(admin_views.sales_moderation), name='admin_moderation'),
    path('map/', login_required(admin_views.interactive_map), name='admin_map'),
    path('sales/', login_required(admin_views.sales_board), name='admin_sales'),
]