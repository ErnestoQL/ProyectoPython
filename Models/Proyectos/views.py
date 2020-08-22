from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from Models.Proyectos.forms import FormularioProyectos
from Models.Proyectos.models import Proyectos


class ProyectosView(HttpRequest):


    def index(request):
            proyectos = Proyectos.objects.all()
            return render(request, 'proyectos_index.html', {'proyectos': proyectos})


    def create(request):
        proyecto = FormularioProyectos()
        return render(request, 'proyectos_create.html', {'form': proyecto})


    def store(request):
        proyecto = FormularioProyectos(request.POST)
        if proyecto.is_valid():
            proyecto.save()
            proyecto = FormularioProyectos()

            return render(request, "proyectos_create.html", {'form': proyecto, "mensaje": "Proyecto registrada exitosamente."})


    def edit(request, id_proyecto):
        proyecto = Proyectos.objects.filter(id=id_proyecto).first()
        form = FormularioProyectos(instance=proyecto)
        return render(request, "proyectos_edit.html", {"form": form, 'proyecto': proyecto})

    def update(request, id_proyecto):
        proyecto = Proyectos.objects.get(pk=id_proyecto)
        form=FormularioProyectos(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
        proyectos = Proyectos.objects.all()
        return render(request, "proyectos_index.html", {"proyectos": proyectos})

    def delete(request, id_proyecto):
        proyecto = Proyectos.objects.get(pk=id_proyecto)
        proyecto.delete()
        proyectos = Proyectos.objects.all()
        return render(request, "proyectos_index.html", {"proyectos": proyectos})
