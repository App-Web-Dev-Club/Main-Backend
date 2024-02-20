from .models import *
from kids.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(KH_Club_Members)
admin.site.register(Faculty)
admin.site.register(Hackathon)
# admin.site.register(HackathonParticipants)
admin.site.register(Student)
# <your_app>/admin.py



class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'name', 'role', 'gender', 'dob', 'contact_number', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'role', 'gender', 'dob', 'contact_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'role', 'gender', 'dob', 'contact_number', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('email', 'name')
    ordering = ('email',)
    list_filter = ('role', 'gender', 'is_staff', 'is_superuser')

admin.site.register(User, CustomUserAdmin)

