from django.shortcuts import render
from django.views.generic import * # todos create, demas... para usuarios...
from django.urls import reverse_lazy # mejorar rendimiento de la app...
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect

from .forms import CustomUserCreationForm # PARA LOS FORMULARIOS...

# Create your views here.

class RegistoUsuarioView(CreateView): # PARA CREAR USUARIO... formulario para mostrar datos formclass.
    form_class = CustomUserCreationForm # una vez la vista genere el formulario tiene que redireccionar a algun lado
    success_url = reverse_lazy("usuarios:login") # redireccionar por la appname.. no hace falta crear nombre de plantilla en usuarios
    template_name = "usuarios/registro.html" # vista creada para direccionar luego agregar ruta en urls de usuarios... 

    @csrf_protect
    def logout_view(request):  # ESTO ES VITAL PARA LOGOUT DE GOOGLE.. SIN ERRORES...
        logout(request) # type: ignore
        return redirect('home') # type: ignore