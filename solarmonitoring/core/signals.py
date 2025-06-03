from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.core.signals import request_started
from django.dispatch import receiver
from django.contrib.sessions.models import Session
import os

@receiver(post_migrate)
def setup_groups(sender, **kwargs):
    # Создаем группы
    groups = {
        'users': ['can_manage_stations'],
        'operators': ['can_moderate', 'can_manage_stations']
    }

    for group_name, perms in groups.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm_codename in perms:
            perm = Permission.objects.get(codename=perm_codename)
            group.permissions.add(perm)


@receiver(request_started)
def clear_sessions_on_startup(sender, **kwargs):
    """
    Очищаем сессии при запуске сервера.
    Используем переменную окружения как флаг, чтобы не очищать при каждом запросе.
    """
    if os.environ.get('DJANGO_SERVER_STARTED') != '1':
        Session.objects.all().delete()
        os.environ['DJANGO_SERVER_STARTED'] = '1'