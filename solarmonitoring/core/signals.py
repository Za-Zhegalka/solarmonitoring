from django.core.signals import request_started
from django.dispatch import receiver
from django.contrib.sessions.models import Session
from django.apps import apps
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
import os



def setup_groups(sender, **kwargs):
    # Проверяем, что модели доступны
    if not apps.ready:
        return

    try:
        view_solar_data_perm = Permission.objects.get(codename='view_solardata')
    except Permission.DoesNotExist:
        print("Не найдены необходимые разрешения.")
        return

    station_viewer_group, created = Group.objects.get_or_create(name='StationViewer')
    station_editor_group, created = Group.objects.get_or_create(name='StationEditor')

    station_viewer_group.permissions.add(view_solar_data_perm)
    # Добавь другие разрешения при необходимости


# Подключаем сигнал
post_migrate.connect(setup_groups, sender=apps.get_app_config('core'))


@receiver(request_started)
def clear_sessions_on_startup(sender, **kwargs):
    """
    Очищаем сессии при запуске сервера.
    Используем переменную окружения как флаг, чтобы не очищать при каждом запросе.
    """
    if os.environ.get('DJANGO_SERVER_STARTED') != '1':
        Session.objects.all().delete()
        os.environ['DJANGO_SERVER_STARTED'] = '1'

