from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),  # Встроенная админка Django
    path('login/', LoginView.as_view(
        template_name='core/auth/login.html',
        redirect_authenticated_user=True,
        extra_context={'next': '/user/dashboard/'}
    ), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', RedirectView.as_view(pattern_name='user_dashboard'), name='home'),
    path('control/', include('core.admin_urls')),  # Админские URL
    path('user/', include('core.user_urls')),  # Пользовательские URL
]

urlpatterns += [
    path('favicon.ico', RedirectView.as_view(url='/static/core/images/favicon.ico')),
]