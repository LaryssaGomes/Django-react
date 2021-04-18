from django.contrib import admin
from django.contrib.auth import admin as auth_admin
# Register your models here.
from .forms import UserChangeForm, UserCreationForm
from .models import Usuario

@admin.register(Usuario)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Usuario