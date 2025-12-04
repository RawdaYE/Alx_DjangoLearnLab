from django.contrib import admin

from .models import CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

    fieldsets= (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )


    add_fieldsets=(
        (None, {
            'classes': ('username', 'email', 'password1', 'password2',
                        'date_of_birth', 'profile_photo', 'is_staff', 'is_active'),
                        }),
    )


    search_fields = ('email', 'username')
    ordering = ('email', )


admin.site.register(CustomUser, CustomUserAdmin)


