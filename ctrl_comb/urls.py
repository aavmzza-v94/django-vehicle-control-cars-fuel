from django.urls import path
from .views import *

# CREAR LA APLICACION VINCULADA LA RUTA EN URLS.PY APP Y SETTINGS.PY
 
urlpatterns = [
    path('mark/',MarkList.as_view(),name="mark_list"), # formatear para que pueda renderizar... mark_list de mark-frm de formulario... ojo!
    path("mark/save",mark_save,name="mark_save"), # mark_save nombre de la vista OSEA FUNCION.. y ruta mark/save para el navegador...
    path("mark/delete/<int:pk>",mark_delete,name="mark_delete"), # pk de la vista....
    path("mark/edit/<int:pk>",mark_edit,name="mark_edit"), # pk de la vista.... luego ir a list para agregar la ruta...
    path('models/',ModeloList.as_view(),name="modelo_list"), # formatear para que pueda renderizar... modelo_list de mark-frm de formulario...
    path('models/new',ModeloNew.as_view(),name="modelo_new"), # este seria para insertar los modelos... crear la plantilla luego..
    path('models/<int:pk>',ModeloEdit.as_view(),name="modelo_edit"), # este seria para insertar los modelos... solo puede llamarse pk sino dara error.. crear la plantilla luego..
    # no olvidar de poner boton en tabla de modelo que renderize el edit de los registros con bootrstrap...
    path('models/delete/<int:pk>',ModeloDelete.as_view(),name="modelo_delete"),
    path('models/modal/<int:pk>',ModeloEditModal.as_view(),name="modelo_edit_modal"), # para modal.. por views... en modelo.html el boton que apunte a modal... OJO
    path('models/modal/new',ModeloNewModal.as_view(),name="modelo_new_modal"), # NO OLVIDAR AGREGAR BOTON! este seria para insertar los modelos... crear la plantilla luego..
    path('models/dt',modelo_dt,name="modelo_dt"), # para la vista de serializacion jsonresponse...

    path("vehicles/",VehiculoList.as_view(),name="vehiculo_list"), # crear la url para la vista de vehiculo... LUEGO CREAR OPCION EN 
    # MENU OSEA EN TEMPLATES CARPETA.. menu.html
    path("vehicles/dt",vehiculo_dt,name="vehiculo_dt"), # para la vista de serializacion jsonresponse...
    path('vehicles/new',VehiculoNewModal.as_view(),name="vehiculo_new"), # NO OLVIDAR AGREGAR BOTON! este seria para insertar los modelos... crear la plantilla luego..
    # ir a vehiculos.html a cargar vehiculo_new..
    path('vehicles/modal/<int:pk>',VehiculoEditModal.as_view(),name="vehiculo_edit"), # para modal.. por views... en vehiculo.html el boton que apunte a modal... OJO
    # IR A PLANTILLA DE VEHICULO.HTML...
    path('vehicles/delete/<int:pk>',VehiculoDelete.as_view(),name="vehiculo_delete"), # LUEGO IR A PLANTILLA VEHICULO.HTML.... y modificar delete
]
