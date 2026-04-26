from django.test import TestCase, SimpleTestCase # EL TEST CASE ES MEJOR...

# Create your tests here.

class HomePageTests(TestCase):
    databases = {'default'}

    def setUp(self):
        self.response = self.client.get("/") # direcciona en la direccion ip inicial...

    def test_url_home(self): # si el response es igual a 200..
        self.assertEqual(self.response.status_code,200)

    def test_plantilla_home(self): # mas acortado...
        self.assertTemplateUsed(self.response,"bases/home.html") # si la plantilla que se usa es la correcta
        self.assertContains(
            self.response,
            "Inicio") # si contiene la palabra inicio manda ok en la plantilla html de home...
        self.assertNotContains(
            self.response,
            "Aplicacion elaborada para Django") # si no contiene manda true...