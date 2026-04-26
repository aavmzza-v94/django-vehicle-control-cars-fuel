from django.contrib import admin
from django.contrib.auth import get_user_model # para usuarios... formularios..
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm # importar desde el fichero las librerias...

# Register your models here.

UsuarioPersonalizado = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm # crear formulario y tipo de formulario..
    form = CustomUserChangeForm # editar...
    model = UsuarioPersonalizado # modelo...
    list_display = [ # desplegar...
        "email",
        "username",
        "is_superuser"
    ]

admin.site.register(UsuarioPersonalizado,CustomUserAdmin) # regitro de superusuario...