from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from Models.Categorias.forms import FormularioCategorias
from Models.Categorias.models import Categorias


class CategoriasView(HttpRequest):


    def index(request):
            categorias = Categorias.objects.all()
            return render(request, 'categorias_index.html', {'categorias': categorias})


    def create(request):
        categoria = FormularioCategorias()
        return render(request, 'categorias_create.html', {'form': categoria})


    def store(request):
        categoria = FormularioCategorias(request.POST)
        if categoria.is_valid():
            categoria.save()
            categoria = FormularioCategorias()

            return render(request, "categorias_create.html", {'form': categoria, "mensaje": "Categoria registrada exitosamente."})


    def edit(request, id_categoria):
        categoria = Categorias.objects.filter(id=id_categoria).first()
        form = FormularioCategorias(instance=categoria)
        return render(request, "categorias_edit.html", {"form": form, 'categoria': categoria,})

    def update(request, id_categoria):
        categoria = Categorias.objects.get(pk=id_categoria)
        form=FormularioCategorias(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
        categorias = Categorias.objects.all()
        return render(request, "categorias_index.html", {"categorias": categorias})

    def delete(request, id_categoria):
        categoria = Categorias.objects.get(pk=id_categoria)
        categoria.delete()
        categorias = Categorias.objects.all()
        return render(request, "categorias_index.html", {"categorias": categorias})
