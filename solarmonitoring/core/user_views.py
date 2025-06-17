from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SolarStation, EnergyData
from django.utils import timezone
from .serializers import StationSerializer
from django.http import JsonResponse
from django.views import View
from .models import Station
from django.core.cache import cache

# Список регионов России (упрощённый)
RUSSIAN_REGIONS = [
    "Центральный федеральный округ",
    "Северо-Западный федеральный округ",
    "Южный федеральный округ",
    "Северо-Кавказский федеральный округ",
    "Приволжский федеральный округ",
    "Уральский федеральный округ",
    "Сибирский федеральный округ",
    "Дальневосточный федеральный округ"
]

@login_required
def profile(request):
    if request.user.is_operator:
        return redirect('admin_profile')
    return render(request, 'core/user/profile.html')

@login_required
def dashboard(request):
    if request.user.is_operator:
        return redirect('admin_dashboard')
    return render(request, 'core/user/dashboard/base.html')

@login_required
def station_management(request):
    """Управление станциями"""
    if request.user.is_operator:
        return redirect('admin_dashboard')

    stations = SolarStation.objects.filter(owner=request.user)
    return render(request, 'core/user/dashboard/station_management.html',
                  {'stations': stations})


@login_required
def monitoring_view(request):
    selected_period = request.GET.get('period', 'week')
    user_id = request.user.id if request.user.is_authenticated else 'anonymous'

    # Генерируем уникальный ключ для кэша на основе пользователя и периода
    cache_key = f'solar_monitoring_data_{user_id}'
    cached_data = cache.get(cache_key)

    if not cached_data:
        cached_data = {}

    # Проверяем, есть ли данные для выбранного периода
    if selected_period not in cached_data:
        # Генерируем новые данные только для текущего периода
        base_value = {
            'day': 1,
            'week': 15,
            'month': 300
        }.get(selected_period, 15)

        if selected_period == 'day':
            energy_data = [round(random.uniform(base_value * 0.6, base_value * 1.4), 2) for _ in range(24)]
        elif selected_period == 'week':
            energy_data = [round(random.uniform(base_value * 0.5, base_value * 1.5), 2) for _ in range(7)]
        elif selected_period == 'month':
            energy_data = [round(random.uniform(base_value * 0.4, base_value * 1.8), 2) for _ in range(30)]

        # Генерация текущих показателей (один раз)
        current_power = round(random.uniform(2.5, 4.0), 1)
        today_energy = round(random.uniform(15, 25), 1)
        comparison = round(random.uniform(-20, 20), 1)

        # Сохраняем всё в кэш
        cached_data[selected_period] = {
            'energy_data': energy_data,
            'current_power': current_power,
            'today_energy': today_energy,
            'comparison': comparison,
        }
        cache.set(cache_key, cached_data, timeout=60*60*24)  # Храним 24 часа

    # Получаем данные из кэша
    data_for_period = cached_data[selected_period]

    # Получаем статусы оборудования (можно оставить рандомными, но тоже можно кэшировать отдельно)
    stations = get_equipment_status()

    context = {
        'energy_data': data_for_period['energy_data'],
        'selected_period': selected_period,
        'current_power': data_for_period['current_power'],
        'today_energy': data_for_period['today_energy'],
        'comparison': data_for_period['comparison'],
        'stations': stations,
    }

    return render(request, 'core/user/dashboard/monitoring.html', context)


@login_required
def recommendations(request):
    """Рекомендации для пользователя"""
    if request.user.is_operator:
        return redirect('admin_dashboard')

    # Заглушка с рекомендациями
    tips = [
        'Оптимальный угол наклона панелей: 35°',
        'Рекомендуется очистить панели от пыли',
        'Пиковая генерация: с 11:00 до 15:00'
    ]
    return render(request, 'core/user/dashboard/recommendations.html',
                  {'tips': tips})


@login_required
def interactive_map(request):
    regions = [
        "Центральный",
        "Северо-Западный",
        "Южный",
        "Северо-Кавказский",
        "Приволжский",
        "Уральский",
        "Сибирский",
        "Дальневосточный"
    ]
    return render(request, 'core/user/interactive_map.html', {'regions': regions})


@login_required
def sales_board(request):
    """Доска объявлений (пользовательская версия)"""
    if request.user.is_operator:
        return redirect('admin_sales')

    ads = [
        {'id': 1, 'title': 'Б/У солнечные панели', 'price': 8000},
        {'id': 2, 'title': 'Контроллер заряда', 'price': 3500}
    ]
    return render(request, 'core/user/sales_board.html', {'ads': ads})


# Получить список всех станций
def get_stations(request):
    stations = Station.objects.all()
    serializer = StationSerializer(stations, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_station_details(request, station_id):
    try:
        station = Station.objects.get(id=station_id)
        serializer = StationSerializer(station)
        return JsonResponse(serializer.data)
    except Station.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)

def get_stations_for_map(request):
    stations = Station.objects.filter(latitude__isnull=False, longitude__isnull=False)
    data = list(stations.values(
        'id', 'name', 'latitude', 'longitude', 'location'
    ))
    return JsonResponse(data, safe=False)

class AddStationView(View):
    def post(self, request):
        # Используем request.POST вместо ручного парсинга тела запроса
        data = request.POST

        try:
            station = Station.objects.create(
                name=data.get('name'),
                location=data.get('location'),
                system_type=data.get('system_type'),
                installed_power=float(data.get('installed_power')),
                installation_date=data.get('installation_date'),

                panel_count=int(data.get('panel_count')),
                panel_type=data.get('panel_type'),
                panel_power=float(data.get('panel_power')),
                panel_manufacturer=data.get('panel_manufacturer'),
                tilt_angle=float(data.get('tilt_angle')),
                orientation=data.get('orientation'),

                inverter_type=data.get('inverter_type'),
                inverter_power=float(data.get('inverter_power')),
                inverter_manufacturer=data.get('inverter_manufacturer'),
                controller_type=data.get('controller_type'),

                battery_type=data.get('battery_type'),
                battery_count=int(data.get('battery_count')),
                battery_capacity_single=float(data.get('battery_capacity_single')),
                battery_voltage=data.get('battery_voltage'),
                battery_manufacturer=data.get('battery_manufacturer'),
            )
            return JsonResponse({'status': 'success', 'id': station.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

class EditStationView(View):
    def post(self, request, station_id):
        try:
            station = Station.objects.get(id=station_id)
            data = request.POST

            # Обновляем все поля
            station.name = data.get('name')
            station.location = data.get('location')
            station.system_type = data.get('system_type')
            station.installed_power = float(data.get('installed_power'))
            station.installation_date = data.get('installation_date')

            station.panel_count = int(data.get('panel_count'))
            station.panel_type = data.get('panel_type')
            station.panel_power = float(data.get('panel_power'))
            station.panel_manufacturer = data.get('panel_manufacturer')
            station.tilt_angle = float(data.get('tilt_angle'))
            station.orientation = data.get('orientation')

            station.inverter_type = data.get('inverter_type')
            station.inverter_power = float(data.get('inverter_power'))
            station.inverter_manufacturer = data.get('inverter_manufacturer')
            station.controller_type = data.get('controller_type')

            station.battery_type = data.get('battery_type')
            station.battery_count = int(data.get('battery_count'))
            station.battery_capacity_single = float(data.get('battery_capacity_single'))
            station.battery_voltage = data.get('battery_voltage')
            station.battery_manufacturer = data.get('battery_manufacturer')

            station.latitude = float(data.get('latitude'))
            station.longitude = float(data.get('longitude'))

            station.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


import random
from datetime import datetime, timedelta

def generate_energy_data(period):
    """Генерирует фейковые данные выработки энергии."""
    base_value = {
        'day': 1,
        'week': 15,
        'month': 300
    }.get(period, 15)

    if period == 'day':
        return [round(random.uniform(base_value * 0.6, base_value * 1.4), 2) for _ in range(24)]
    elif period == 'week':
        return [round(random.uniform(base_value * 0.5, base_value * 1.5), 2) for _ in range(7)]
    elif period == 'month':
        return [round(random.uniform(base_value * 0.4, base_value * 1.8), 2) for _ in range(30)]


def get_equipment_status():
    statuses = [('bg-success', 'Норма'), ('bg-warning text-dark', 'Требует внимания')]
    return [(station.name, random.choice(statuses)) for station in SolarStation.objects.all()]


def monitoring_view(request):
    selected_period = request.GET.get('period', 'week')
    energy_data = generate_energy_data(selected_period)

    current_power = round(random.uniform(2.5, 4.0), 1)
    today_energy = round(random.uniform(15, 25), 1)
    comparison = round(random.uniform(-20, 20), 1)

    stations = get_equipment_status()

    context = {
        'energy_data': energy_data,
        'selected_period': selected_period,
        'current_power': current_power,
        'today_energy': today_energy,
        'comparison': comparison,
        'stations': stations,
    }
    return render(request, 'core/user/dashboard/monitoring.html', context)