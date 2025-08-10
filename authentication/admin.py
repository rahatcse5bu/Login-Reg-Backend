from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Fields to display in the list view
    list_display = (
        'email', 'username', 'first_name', 'last_name',
        'university', 'blood_group', 'gender', 'is_active', 'date_joined'
    )
    
    # Fields to filter by
    list_filter = (
        'is_active', 'is_staff', 'is_superuser', 'gender',
        'blood_group', 'university', 'date_joined'
    )
    
    # Fields to search by
    search_fields = ('email', 'username', 'first_name', 'last_name', 'mobile_no')
    
    # Ordering
    ordering = ('-date_joined',)
    
    # Fields for the add/edit form
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Personal Info', {
            'fields': (
                'first_name', 'last_name', 'gender', 'date_of_birth',
                'mobile_no', 'blood_group', 'address'
            )
        }),
        ('Academic Info', {
            'fields': ('university',)
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    # Fields for the add form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'first_name', 'last_name',
                'password1', 'password2'
            ),
        }),
        ('Additional Info', {
            'classes': ('wide',),
            'fields': (
                'university', 'blood_group', 'mobile_no',
                'gender', 'date_of_birth'
            ),
        }),
    )
    
    readonly_fields = ('date_joined', 'last_login')
