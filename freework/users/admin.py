from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User
from .forms import UserChangeForm, UserCreationForm


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        *AuthUserAdmin.fieldsets[2:],
    )
    list_display = ("username", "email", "name", "is_staff")
    search_fields = ("username", "name", "email")
    ordering = ["username"]
