from django.urls import path
from . import user_views  # Изменено с solarmonitoring.core.templates
from django.contrib.auth.decorators import login_required
from .user_views import get_stations, AddStationView, get_station_details, EditStationView

urlpatterns = [
    path('profile/', login_required(user_views.profile), name='user_profile'),
    path('dashboard/', login_required(user_views.dashboard), name='user_dashboard'),
    path('dashboard/stations/', login_required(user_views.station_management), name='user_stations'),
    path('dashboard/monitoring/', login_required(user_views.monitoring), name='user_monitoring'),
    path('dashboard/recommendations/', login_required(user_views.recommendations), name='user_recommendations'),
    path('map/', login_required(user_views.interactive_map), name='user_map'),
    path('sales/', login_required(user_views.sales_board), name='user_sales'),
    path('stations/', get_stations, name='get_stations'),
    path('stations/add/', AddStationView.as_view(), name='add_station'),
    path('stations/<int:station_id>/', get_station_details, name='get_station_details'),
    path('stations/edit/<int:station_id>/', EditStationView.as_view(), name='edit_station'),
]