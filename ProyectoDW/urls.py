"""ProyectoDW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from Models.Categorias.views import CategoriasView
from Models.Lideres.views import LideresView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('categorias/', CategoriasView.index, name='categorias'),
    path('registrar-categoria/', CategoriasView.create, name='registrarCategoria'),
    path('guardar-categoria/', CategoriasView.store, name='guardarCategoria'),
    path('editar-categoria/<int:id_categoria>', CategoriasView.edit, name='editarCategoria'),
    path('actualizar-categoria/<int:id_categoria>', CategoriasView.update, name='actalizarCategoria'),
    path('eliminar-categoria/<int:id_categoria>', CategoriasView.delete, name='eliminarCategoria'),


    path('lideres/', LideresView.index, name='lideres'),
    path('registrar-lider/', LideresView.create, name='registrarLider'),
    path('guardar-lider/', LideresView.store, name='guardarLider'),
    path('editar-lider/<int:id_lider>', LideresView.edit, name='editarLider'),
    path('actualizar-lider/<int:id_lider>', LideresView.update, name='actalizarLider'),
    path('eliminar-lider/<int:id_lider>', LideresView.delete, name='eliminarLider'),
]
