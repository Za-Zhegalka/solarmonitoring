from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SolarStation, EnergyData
from django.utils import timezone
from .serializers import StationSerializer
from django.http import JsonResponse
from django.views import View
from .models import Station
from django.core.cache import cache
from .models import Recommendation

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


def generate_all_data():
    data = {}

    now = timezone.now()
    today = now.date()

    # Генерация базового значения
    yesterday_energy = round(random.uniform(15, 25), 1)
    base_daily_energy = round(random.uniform(yesterday_energy * 0.8, yesterday_energy * 1.3), 1)
    comparison = round((base_daily_energy - yesterday_energy) / yesterday_energy * 100, 1)
    current_power = round(random.uniform(2.5, 4.0), 1)

    # График за день — только до текущего времени
    current_hour = now.hour + 1  # Включая текущий час
    daily_data = [round(random.uniform(current_power * 0.6, current_power * 1.4), 2) for _ in range(current_hour)]
    daily_labels = [f"{hour}:00" for hour in range(current_hour)]

    # График за неделю — с понедельника или с недели назад, заканчивая сегодня
    week_start = today - timedelta(days=today.weekday())
    days_week = [(week_start + timedelta(days=i)) for i in range((today - week_start).days + 1)]
    weekly_data = [round(random.uniform(base_daily_energy * 0.7, base_daily_energy * 1.3), 2) for _ in range(len(days_week))]
    weekly_data[-1] = base_daily_energy  # Сегодняшнее значение
    weekly_labels = [day.strftime("%a") for day in days_week]

    # График за месяц — с 1 числа до сегодня
    first_day_of_month = today.replace(day=1)
    num_days_month = (today - first_day_of_month).days + 1
    days_month = [(first_day_of_month + timedelta(days=i)) for i in range(num_days_month)]
    monthly_data = [round(random.uniform(base_daily_energy * 0.5, base_daily_energy * 1.5), 2) for _ in range(num_days_month)]
    monthly_data[-1] = base_daily_energy  # Сегодняшнее значение
    monthly_labels = [day.day for day in days_month]

    data['day'] = {
        'energy_data': daily_data,
        'labels': daily_labels,
        'current_power': current_power,
        'today_energy': base_daily_energy,
        'comparison': comparison,
    }

    data['week'] = {
        'energy_data': weekly_data,
        'labels': weekly_labels,
        'current_power': current_power,
        'today_energy': base_daily_energy,
        'comparison': comparison,
    }

    data['month'] = {
        'energy_data': monthly_data,
        'labels': monthly_labels,
        'current_power': current_power,
        'today_energy': base_daily_energy,
        'comparison': comparison,
    }

    return data


def monitoring_view(request):
    selected_period = request.GET.get('period', 'week')
    user_id = request.user.id if request.user.is_authenticated else 'anonymous'

    cache_key = f'solar_monitoring_data_{user_id}'
    cached_data = cache.get(cache_key)

    if not cached_data:
        cached_data = generate_all_data()
        cache.set(cache_key, cached_data, timeout=60 * 60 * 24)

    data_for_period = cached_data[selected_period]

    last_update_key = f'status_last_updated_{user_id}'
    last_updated = cache.get(last_update_key)

    now = timezone.now()
    if not last_updated or (now - last_updated).seconds > 300:
        update_equipment_status()
        cache.set(last_update_key, now, timeout=60 * 60 * 24)

    stations = get_equipment_status()

    context = {
        'energy_data': data_for_period['energy_data'],
        'selected_period': selected_period,
        'current_power': data_for_period['current_power'],
        'today_energy': data_for_period['today_energy'],
        'comparison': data_for_period['comparison'],
        'stations': stations,
        'data': cached_data,  # Передаем все данные для использования в шаблоне
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


def update_equipment_status():
    now = timezone.now()
    stations = Station.objects.all()

    for station in stations:
        if station.force_attention_until and station.force_attention_until > now:
            # Статус не меняется, если еще действует принудительное состояние
            continue

        # 10% шанс перейти в "Требует внимания"
        if random.random() < 0.1:  # 10%
            station.status = 'attention'
            # Устанавливаем срок действия статуса на 1 час
            station.force_attention_until = now + datetime.timedelta(minutes=60)
        else:
            if not station.force_attention_until or station.force_attention_until <= now:
                # Только если не зафиксировано принудительное состояние
                station.status = 'normal'

        station.save()

def get_equipment_status():
    stations = Station.objects.all()
    result = []

    for station in stations:
        if station.status == 'normal':
            badge_class, label = 'bg-success', 'Норма'
        else:
            badge_class, label = 'bg-warning text-dark', 'Требует внимания'

        result.append((
            station.name,
            station.last_checked.strftime('%d.%m %H:%M'),
            badge_class,
            label
        ))

    return result

def recommendations_view(request):
    recommendations = Recommendation.objects.all().order_by('-date')
    return render(request, 'core/user/dashboard/station_management.html', {
        'recommendations': recommendations
    })