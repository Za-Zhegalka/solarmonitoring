from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

# Проверка, что пользователь - администратор
def check_admin(user):
    return user.is_authenticated and (user.is_operator or user.is_superuser)

# ----- Профиль -----
@login_required
@user_passes_test(check_admin)
def admin_profile(request):
    return render(request, 'core/admin/profile.html')

@login_required
@user_passes_test(check_admin)
def admin_user_list(request):
    return render(request, 'core/admin/dashboard/user_list.html')

@login_required
@user_passes_test(check_admin)
def admin_support_requests(request):
    return render(request, 'core/admin/dashboard/support_requests.html')

@login_required
@user_passes_test(check_admin)
def admin_action_analytics(request):
    return render(request, 'core/admin/dashboard/action_analytics.html')

@login_required
@user_passes_test(check_admin)
def admin_sales_moderation(request):
    return render(request, 'core/admin/dashboard/sales_moderation.html')

# ----- Интерактивная карта -----
@login_required
@user_passes_test(check_admin)
def admin_interactive_map(request):
    return render(request, 'core/admin/interactive_map.html')

# ----- Доска объявлений -----
@login_required
@user_passes_test(check_admin)
def admin_sales_board(request):
    return render(request, 'core/admin/sales_board.html')

def base(request):
    return render(request, 'core/base.html')

@csrf_exempt  # Временно отключаем CSRF для тестирования
def custom_logout(request):
    logout(request)
    request.session.flush()  # Полная очистка сессии
    return redirect('login')