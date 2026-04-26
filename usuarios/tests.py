from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm # importar para poder verificar el formulario.... y USUARIOS...
from .views import RegistroUsuarioView # importar desde la vista... 


# Create your tests here.

class CustomUserTests(TestCase):
    def test_crear_usuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_user(
            username = "debsconsultores",
            email = "debsconsultores@gmail.com",
            password = "123",
            firstname = "debs",
        )

        # Que esperamos?
        self.assertEqual(usr.username,"debsconsultores") # probar si son iguales username y la cadena...
        self.assertEqual(usr.email,"debsconsultores@gmail.com")
        self.assertTrue(usr.is_active) # si es false tiene fallo...
        self.assertFalse(usr.is_staff)
        self.assertFalse(usr.is_superuser)

    def test_crear_superusuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_superuser( # objects es el manager por default.... que trae y createsuperuser son metodos creados en manager user
            username = "debsconsultores",
            email = "debsconsultores@gmail.com",
            password = "123",
            firstname = "debs",
        )

        # Que esperamos?
        self.assertEqual(usr.username,"debsconsultores") # probar si son iguales username y la cadena...
        self.assertEqual(usr.email,"debsconsultores@gmail.com")
        self.assertTrue(usr.is_active) # si es false tiene fallo...
        self.assertTrue(usr.is_staff)
        self.assertTrue(usr.is_superuser)


class RegistroUsuarioTest(TestCase): # VERIFICAR LA CONEXION Y SI ESTA HABILITADO EL REGISTRO DE FORMULARIO EN HTTP
    def setUp(self):
        url = reverse("usuarios:registro")
        self.response = self.client.get(url)

    def test_plantilla_registro(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,"usuarios/registro.html")
        self.assertContains(self.response,"Registro")
        self.assertNotContains(self.response,"Bienvenido")

    def test_registro_form(self):
        form = self.response.context.get("form")  # si se puede conectar al formulario y registro...
        self.assertIsInstance(form,CustomUserCreationForm)
        self.assertContains(self.response,"csrfmiddlewaretoken")
    
    def test_registro_vista(self):
        view = resolve("/usuarios/registro/") # si se puede conectar a vista...
        self.assertEqual(view.func.__name__,RegistroUsuarioView.as_view().__name__)
