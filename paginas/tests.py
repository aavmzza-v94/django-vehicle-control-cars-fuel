from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.

class AboutPageTests(TestCase):
    databases = {'default'}

    def SetUp(self):
        self.response = self.client.get("/pages/about")

    def test_url_about(self): # si el response es igual a 200..
        self.assertEqual(self.response.status_code,200)

    def test_html_about(self): # mas acortado...
        self.assertTemplateUsed(self.response,"paginas/about.html") # si la plantilla que se usa es la correcta
        self.assertContains(
            self.response,
            "Aplicacion elaborada para Django")
        self.assertNotContains(
            self.response,
            "Aplicacion elaborada para Django")
    

#    def test_existe_ruta(self):
#        response = self.client.get("/pages/about")
#        self.assertEqual(response.status_code,200) # para ver si la pagina esta habilitada y cargada sin error 404 o 400..

#    def test_nombre_ruta(self):
#        response = self.client.get(reverse("/pages/about")) # baneando el archivo de rutas... OJO peticion... pregunta por pagina
#        self.assertEqual(response.status_code,200)

#    def test_plantilla_contiene_html(self):
#        response = self.client.get(reverse("/pages/about")) # baneando el archivo de rutas... OJO peticion... pregunta por pagina
#        self.assertContains(response,"Aplicacion elaborada para Django") # si contiene el html dicho texto devuelve true....

#    def test_plantilla_no_contiene_html(self):
#        response = self.client.get(reverse("/pages/about")) # baneando el archivo de rutas... OJO peticion... pregunta por pagina
#        self.assertNotContains(response,"Aplicacion elaborada para Django") # si contiene el html dicho texto devuelve true si no contiene....


        # docker-compose exec web python manage.py test paginas  en cmd...