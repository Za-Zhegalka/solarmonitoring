from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


def group_required(*group_names):
    def in_groups(u):
        if u.is_authenticated:
            if u.is_superuser or u.groups.filter(name__in=group_names).exists():
                return True
        raise PermissionDenied

    return user_passes_test(in_groups)