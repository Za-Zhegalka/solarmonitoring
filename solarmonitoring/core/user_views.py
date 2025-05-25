from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SolarStation, EnergyData
from django.utils import timezone
from datetime import timedelta


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
def monitoring(request):
    """Мониторинг данных"""
    if request.user.is_operator:
        return redirect('admin_dashboard')

    # Пример данных для графика (последние 7 дней)
    end_date = timezone.now()
    start_date = end_date - timedelta(days=7)

    energy_data = EnergyData.objects.filter(
        station__owner=request.user,
        timestamp__range=(start_date, end_date)
    ).order_by('timestamp')

    return render(request, 'core/user/dashboard/monitoring.html',
                  {'energy_data': energy_data})


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
def community(request):
    """Сообщество пользователей"""
    if request.user.is_operator:
        return redirect('admin_community')
    return render(request, 'core/user/community.html')


@login_required
def interactive_map(request):
    """Интерактивная карта (пользовательская версия)"""
    if request.user.is_operator:
        return redirect('admin_map')

    user_stations = SolarStation.objects.filter(owner=request.user)
    return render(request, 'core/user/interactive_map.html',
                  {'stations': user_stations})


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