from . import views
from .views import custom_logout
from django.urls import include, path

urlpatterns = [
    # Админские URLs
    path('base/', views.base, name='base'),
    path('base/profile/', views.admin_profile, name='admin_profile'),
    path('base/dashboard/users/', views.admin_user_list, name='admin_user_list'),
    path('base/dashboard/support/', views.admin_support_requests, name='admin_support'),
    path('base/dashboard/analytics/', views.admin_action_analytics, name='admin_analytics'),
    path('base/dashboard/moderation/', views.admin_sales_moderation, name='admin_moderation'),
    path('base/map/', views.admin_interactive_map, name='admin_map'),
    path('base/sales/', views.admin_sales_board, name='admin_sales'),
    path('logout/', custom_logout, name='logout'),
    path('user/', include('core.user_urls'))
]