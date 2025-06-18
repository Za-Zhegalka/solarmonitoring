from django.contrib import admin
from .models import User
from .models import Recommendation

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('groups', 'is_operator')
    list_display = ('username', 'get_groups')

    def get_groups(self, obj):
        return ", ".join([g.name for g in obj.groups.all()])
    get_groups.short_description = 'Groups'

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('date', 'text', 'recommendation_type', 'status')
    list_filter = ('status', 'recommendation_type')
    search_fields = ('text',)