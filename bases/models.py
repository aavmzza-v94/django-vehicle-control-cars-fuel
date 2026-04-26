from django.db import models
from django.contrib.auth import get_user_model # modelo de usuario a usar


# Create your models here. CREAR DEFINICION..


User = get_user_model() # modelo de usuario personalizado, se inicia con getusermodel...

# crear Modelo

class ClaseModelo(models.Model): # heredara de Model... propiedad en django...
    estado = models.BooleanField(default=True) # true o false si el registro esta activo o no
    uc = models.ForeignKey(User, on_delete=models.CASCADE,related_name="+") # user create, poner siempre + para relacionar, CASCADE BORRAR
    fc = models.DateTimeField(auto_now_add=True) # insertar fecha y hora automaticamente, PARA MIGRAR... A TABLA... cambio campo de fecha...
    # user modificar
    um = models.ForeignKey(User, on_delete=models.SET_NULL,related_name="+",
                           blank=True, null=True) # user create, poner siempre + para relacionar, SET ES FIJAR, registro en form no sea requerido
    fm = models.DateTimeField(auto_now=True) # modificar fecha del sistema... afecta fm nomas...

    # al migrar esto, django crea una tabla llamada ClaseModelo.. la meta es usar la clasr para heredar a los demas modelos
# PARA ELLO CREAR ABSTRACT EN CLASE META...

    class Meta:
        abstract = True # si no se agrega al modelo, django al crear la migracion... crea tabla, lo que queremos es clase primaria.. no tabla
    # AGREGAR SI O SI!!! no crea la tabla! migracion en aplicacion bases... NO OLVIDAR TABULAR... SINO CREA LA MIGRACION... INDENTAR



