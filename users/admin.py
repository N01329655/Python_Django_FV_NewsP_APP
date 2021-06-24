from django.contrib import admin

# my imports
from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # to display preferred columns
    list_display = ['email', 'username', 'age', 'is_staff', ]


admin.site.register(CustomUser, CustomUserAdmin)
