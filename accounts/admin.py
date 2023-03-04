from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm  # dokmeye add kardan yek user
    form = CustomUserChangeForm  # formi ke haminjuri aval be ma neshun mide
    model = CustomUser
    list_display = ['username', 'age', 'is_staff','email']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age', 'phone',), }),)  # baraye ChangeForm

    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('age', 'phone',), }),)  # baraye CreationForm


admin.site.register(CustomUser, CustomUserAdmin)

