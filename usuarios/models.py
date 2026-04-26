from django.contrib.auth.models import AbstractUser, PermissionsMixin # permisos tambien..
from django.db import models
from django.utils.translation import gettext_lazy as _ # para la traducciones en paginas de idiomas abreviando como _ porque es largo
from .manager import CustomUserManager # importar . es local...


# Create your models here.
# class Usuario(AbstractUser):
#    ... # esto era modelo usuario por default... se usaba al principio para prueba nomas...

class Usuario(AbstractUser):
    email = models.EmailField(unique=True) # agregar campo unico...
    username = models.CharField(_("Nombre de Usuario"), max_length=150) # caracteres...
    first_name = models.CharField(_("Nombres"), max_length=150)
    last_name = models.CharField(_("Apellido"), max_length=150)
    is_staff = models.BooleanField(default=False) # se creara en falso con el create superuser tomara True...
    is_active = models.BooleanField(default=True) # aca poner para que active directo al logearse con google...
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager() # el user tendra un manager... ESTABLECERLO..

    USERNAME_FIELD = "email" # el campo principal es el email...
    REQUIRED_FIELDS = ['username','first_name']  

    # el metodo _str_ humaniza los caracteres de los campos de usuarios convierte de HEX
    def __str__(self):
        return self.email