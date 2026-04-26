from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse # devolver a la plantilla un texto...
from django.views.generic import * # vista generica... este seria para proyectar con la ip directo....
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse_lazy # REDIRECCIONAR cargar una lista, una URL...
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin # para los permisos A MARKLIST Y MODELOLIST... marcas y modelos... que no fije sin login

# camara_app/views.py

# from django.shortcuts import render
# from django.http import StreamingHttpResponse
# from django.views.decorators import gzip
# import cv2  # COMENTAR PORQUE NO RECONOCE EL DOCKER... SINO SE USA AL MENOS...



# Create your views here.

# Función generadora para capturar fotogramas de la cámara
# def gen_camera_stream():
#     index = 0
#     max_index = 10  # Máximo número de dispositivos a probar
#     found_devices = []  # Lista para almacenar los números de dispositivos encontrados
#     print("Buscando dispositivos de cámara...")
    
#     while index < max_index:
#         # Intenta abrir el dispositivo de cámara con el índice actual
#         cap = cv2.VideoCapture(index)
        
#         if cap.isOpened():
#             # Si la cámara se abre correctamente, añade el número de dispositivo a la lista
#             print(f"Dispositivo de cámara encontrado: {index}")
#             found_devices.append(index)  # Añade el índice a la lista
#             cap.release()  # Libera el dispositivo de cámara
#         else:
#             # Si no se puede abrir, no hay cámara en este índice
#             print(f"No se encontró cámara en el índice: {index}")
        
#         index += 1

#     if not found_devices:
#         print("No se encontraron dispositivos de cámara.")
    
#     cap = found_devices[0]  # Índice de la cámara (ajusta según sea necesario)
#     if not cap.isOpened():
#         print("Error: No se puede abrir la cámara.")
#         return

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: No se puede leer el fotograma.")
#             break

#         ret, jpeg = cv2.imencode('.jpg', frame)
#         if not ret:
#             print("Error: No se puede codificar el fotograma.")
#             break

#         frame_bytes = jpeg.tobytes()

#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')

#     cap.release()

# # Vista para manejar la transmisión de video
# @gzip.gzip_page
# def video_feed(request):
#     return StreamingHttpResponse(gen_camera_stream(), content_type='multipart/x-mixed-replace; boundary=frame')

# # Vista que renderiza el home.html
# def home(request):
#     return render(request, 'home.html')  # Renderiza tu plantilla principal


# PARA TRABAJAR CON VERSIONES DJANGO MAS NUEVAS.. CREAR FUNCION

def is_ajax(request): # determinar si es ajax o no la peticion
    return request.META.get('HTTP_X_REQUEST_WITH') == 'XMLHttpRequest' # VALOR A TOMAR PARA SABER LA PEETICION
    # ver si la peticion es de tipo H...


# crear MIXIN
class MixinFormInvalid:
    def form_invalid(self,form): # cuando un formulario no pasa y contiene errores... respuesta...
        response = super().form_invalid(form) # ejecucion de la clase padre.. por super() manejo de errores 
        if is_ajax(request=self.request): # devuelve si la peticion es ajax
            return JsonResponse(form.errors,status=400) # se retorna error...
        else: # si no es peticion AJAX SE RETORNA RESPONSE ORIGINAL
            return response
        
# CREAR LOGIN REQUIRED MIXIN PARA PERMISOS... CLASE HEREDADA DE TODOS LOS MIXIN..
# sirve todo esto para importar a las demas vistas.... en ctrl_comb views...
        
class SinAutorizacion(LoginRequiredMixin,PermissionRequiredMixin,MixinFormInvalid):
    login_url = "bases:login" # si o si para mixin... propiedad, que vaya
    raise_exception = False # propiedad para autenticar.. ESTO ES PARA QUE NO LEVANTE ERROR... EL 403 O 404..
    redirect_field_name = "redirect_to" # redirigir al usuario despues de autenticarse...
    def handle_no_permission(self): # importar de django http el http response redirect... para poder redireccionar si es anonimo..
         # que rediriga al login url...
        if not self.request.user == AnonymousUser():  # si el user no es anonimo.. ya tiene login o esta autenticado pero no permiso
            self.login_url = "pages:forbidden" # sobreescrcibir login_url...
        return HttpResponseRedirect(reverse_lazy(self.login_url)) # si es o no anonimo... no hace falta redirigir a login... con reverselazy
         # la utlima linea que no se logee sino que presente la pantalla al user si es anonimo...

def primera_vista(request): # viene los datos del frontend de la plantilla formularios, var, etc del usuario logeado
    return HttpResponse("Hola Mundo")

class HomeView(TemplateView): # hereda de templateview
    template_name = "bases/home.html" # para la plantilla poder visualizar... indicar el directorio correctamente... para que direccione


# CREAR MIXIN PARA EDITAR, BORRAR Y CREAR REGISTROS... DE MODELOS.... POR VISTAS CLASES... A VIEWS DE CTRL_COMB SIN NECESIDAD
# DE ESCRIBIR MUCHO CODIGO PARA CADA CLASE..

class MixinSaveUser:
    def form_valid(self, form): # recibe el formulario.... OJO INDENTADO....
        print(f"*********{form.instance.id} --- {self.request.user.id} *****************") 
        # f seria formato para que en la impresion se acepte tanto caracteres como numerico denotado por {}
        # el id seria para ver el formulario... y luego ver si existe el id... por user...
        if form.instance.id : # si el formulario existe
            form.instance.um = self.request.user # en el campo usuario modifica extrae el id...  si tiene id se modifica registro
        else: # SINO la instancia del formulario del frontend no trae un id...
            form.instance.uc = self.request.user # poner valor al usuario crea, si no trae id se crea registro

        return super().form_valid(form) # enviar el formulario...
    # IMPORTAR LA CLASE A VIEWS DE CTRL_COMB... se invoca a mixinsaveuser en la clase y def... con sinautorizacion...