from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import User, SolarStation

def check_admin(user):
    return user.is_authenticated and user.is_operator

@user_passes_test(check_admin)
def dashboard(request):
    """Главная панель администратора"""
    context = {
        'user_count': User.objects.count(),
        'station_count': SolarStation.objects.count()
    }
    return render(request, 'core/admin/dashboard/base.html', context)

@user_passes_test(check_admin)
def profile(request):
    """Профиль администратора"""
    return render(request, 'core/admin/profile.html', {'user': request.user})

@user_passes_test(check_admin)
def user_list(request):
    """Список пользователей"""
    users = User.objects.all()
    return render(request, 'core/admin/dashboard/user_list.html', {'users': users})

@user_passes_test(check_admin)
def support_requests(request):
    """Запросы в поддержку"""
    # Заглушка для демонстрации
    requests = [
        {'id': 1, 'subject': 'Проблема с подключением', 'status': 'Новый'},
        {'id': 2, 'subject': 'Вопрос по оплате', 'status': 'В обработке'}
    ]
    return render(request, 'core/admin/dashboard/support_requests.html',
                {'requests': requests})

@user_passes_test(check_admin)
def action_analytics(request):
    """Аналитика действий"""
    # Заглушка для демонстрации
    stats = {
        'active_users': 42,
        'new_registrations': 5,
        'stations_added': 3
    }
    return render(request, 'core/admin/dashboard/action_analytics.html',
                {'stats': stats})

@user_passes_test(check_admin)
def sales_moderation(request):
    """Модерация объявлений"""
    # Заглушка для демонстрации
    ads = [
        {'id': 1, 'title': 'Продажа панелей', 'status': 'На модерации'},
        {'id': 2, 'title': 'Услуги монтажа', 'status': 'Одобрено'}
    ]
    return render(request, 'core/admin/dashboard/sales_moderation.html',
                {'ads': ads})

@user_passes_test(check_admin)
def interactive_map(request):
    """Интерактивная карта станций"""
    stations = SolarStation.objects.all()[:10]  # Ограничение для демонстрации
    return render(request, 'core/admin/interactive_map.html',
                {'stations': stations})

@user_passes_test(check_admin)
def sales_board(request):
    """Доска объявлений (админ)"""
    ads = [
        {'id': 1, 'title': 'Солнечные панели 300W', 'price': 15000},
        {'id': 2, 'title': 'Инвертор 5kW', 'price': 25000}
    ]
    return render(request, 'core/admin/sales_board.html', {'ads': ads})