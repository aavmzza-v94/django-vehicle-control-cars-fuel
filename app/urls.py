"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',include('bases.urls')),
    path('admin/', admin.site.urls),
    path('pages/', include('paginas.urls')),
    path('usuarios/', include('usuarios.urls')), # mapear rutas... en principal...
    path('accounts/', include('allauth.urls')), # agregamos conjunto de rutas accounts... para login especifico... urls de plugin allauth
    # luego hacer la migracion...
    path('control/', include(('ctrl_comb.urls','control'),namespace="control")), # VINCULAR RUTA DE LA APLICACION... en la carpeta ctrl_comb y urls.py...
    # por eso el control:.... se abrevia nomas en el menu.html hay mucho de eso...
]
