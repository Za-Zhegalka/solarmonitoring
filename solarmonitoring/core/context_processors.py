def user_groups(request):
    return {
        'user_groups': list(request.user.groups.values_list('name', flat=True))
    }