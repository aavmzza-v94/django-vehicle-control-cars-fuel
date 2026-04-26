from django.test import TestCase
from django.urls import reverse # usamos las rutas...
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import Permission

from .models import Mark, Modelo # importar todo de modelos


# Create your tests here.

class ModeloTests(TestCase): # Test de modelos...
    @classmethod  # permite agregar clases con objetos para tests... PROPIEDAD
    def setUpTestData(clase): # metodo como classmethod recibe un objeto clase...
        clase.modelo = Modelo.objects.create( # tendra modelo  object...
            mark = Mark.objects.create(descript = "Toyota"), # La marca creara por object... para probar descript Toyota
            descript = "Rush"  # descripcion del modelo.... esto solo para probar... inicializar datos
        )
        clase.user = get_user_model().objects.create_user(
            username= "agus",
            email= "aavmzza@gmail.com",
            first_name = "agus",
            password= "agus123",
        )
        clase.ver_modelo = Permission.objects.get(
            codename = "view_modelo"
        )

    def test_lista(self): # test del listado
        self.assertEqual(self.modelo.descript,"Rush") # si en el modelo la descripcion tiene la palabra Rush
        self.assertEqual(self.modelo.mark.descript,"Toyota") # lo mismo para la marca Toyota... se compara self.modelo con la palabra Rush
        # DEBE DEVOLVER SIN PROBLEMA...

    def test_vista_model_logout(self): # LOGOUT DE MODELOS...
        self.client.logout() # CIERRE DE SESION
        response = self.client.get(reverse("control:modelo_list")) # para el logout... redireccion regresar..
        self.assertEqual(response.status_code,302) # en caso de cierre de sesion en la consola..



    def test_vista_modelo_usuario_autenticado(self): # PROBAR VISTA DE MODELOS...
        # self.client.logout() 
        self.client.login(email="aavmzza@gmail.com",password="agus123") # para el test de login...
        # asignar el permiso
        self.user.user_permissions.add(self.ver_modelo) # para agregar...
        response = self.client.get(reverse("control:modelo_list")) # INVOCAR LA RUTA... POR CLIENT POR MODELO LIST...
        self.assertEqual(response.status_code,200) # STATUS CODE.... 200 RESPONSE ES DE HTTP
        # print(response.content.decode('utf-8')) # DECODIFICAR...
        # self.assertContains(response,"Rush") # SI CONTIENE LA PALABRA RUSH...
        self.assertTemplateUsed(response,"ctrl_comb/modelo_list.html") # VERIFICAR LA PLANTILLA

        # LOGOUT DE MARCA....

    def test_vista_marca_logout(self): # LOGOUT DE MODELOS...
        self.client.logout() # CIERRE DE SESION
        response = self.client.get(reverse("control:mark_list")) # para el logout... redireccion regresar..
        self.assertEqual(response.status_code,302) # en caso de cierre de sesion en la consola..
    
    
    def test_vista_marca_usuario_autenticado(self):
        # self.client.logout()
        self.client.login(email="aavmzza@gmail.com",password="agus123") # para el test de login...
        response = self.client.get(reverse("control:mark_list"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Toyota") # SI CONTIENE LA PALABRA TOYOTA...
        self.assertTemplateUsed(response,"ctrl_comb/mark_list.html") # VERIFICAR LA PLANTILLA

    # AHORA PARA MODAL

    def test_vista_modal(self):
        response = self.client.get(reverse("control:modelo_edit_modal",kwargs={'pk':self.modelo.id})) # kwargs es para arreglo... por pk... SI RESPONDE EL HTML....
        self.assertEqual(response.status_code,200) # status http... de la pagina o ruta
        self.assertContains(response,"Rush") # SI CONTIENE LA PALABRA RUSH...
        self.assertTemplateUsed(response,"ctrl_comb/modelo_modal.html") # VERIFICAR LA PLANTILLA


    
