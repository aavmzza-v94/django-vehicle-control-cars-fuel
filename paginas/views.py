from django.shortcuts import render 
from django.views.generic import *

# Create your views here.
# app_name="pages" # al nombrar url ... pages:about o forbidden...
class AboutView(TemplateView):
    template_name = "paginas/about.html" # busca una plantilla que este en directorio paginas... por vista...
    # sino encuentra busca en templates general... sino mandara un error que no existe la plantilla

class ForbiddenView(TemplateView):
    template_name = "paginas/forbidden.html" # busca una plantilla que este en directorio paginas... por vista...
    # sino encuentra busca en templates general... sino mandara un error que no existe la plantilla, registrar en urls.py RUTA