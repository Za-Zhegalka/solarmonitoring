from django.urls import path
from . import user_views  # Изменено с solarmonitoring.core.templates
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('profile/', login_required(user_views.profile), name='user_profile'),
    path('dashboard/', login_required(user_views.dashboard), name='user_dashboard'),
    path('dashboard/stations/', login_required(user_views.station_management), name='user_stations'),
    path('dashboard/monitoring/', login_required(user_views.monitoring), name='user_monitoring'),
    path('dashboard/recommendations/', login_required(user_views.recommendations), name='user_recommendations'),
    path('map/', login_required(user_views.interactive_map), name='user_map'),
    path('sales/', login_required(user_views.sales_board), name='user_sales'),
]