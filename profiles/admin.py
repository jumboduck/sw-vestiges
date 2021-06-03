from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'is_anim',
        'is_active',
    )

    ordering = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
