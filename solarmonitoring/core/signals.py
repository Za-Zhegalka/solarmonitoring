from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver

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