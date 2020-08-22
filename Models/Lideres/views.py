from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from Models.Lideres.forms import FormularioLideres
from Models.Lideres.models import Lideres


class LideresView(HttpRequest):


    def index(request):
            lideres = Lideres.objects.all()
            return render(request, 'lideres_index.html', {'lideres': lideres})


    def create(request):
        lider = FormularioLideres()
        return render(request, 'lideres_create.html', {'form': lider})


    def store(request):
        lider = FormularioLideres(request.POST)
        if lider.is_valid():
            lider.save()
            lider = FormularioLideres()

            return render(request, "lideres_create.html", {'form': lider, "mensaje": "Lider registrada exitosamente."})


    def edit(request, id_lider):
        lider = Lideres.objects.filter(id=id_lider).first()
        form = FormularioLideres(instance=lider)
        return render(request, "lideres_edit.html", {"form": form, 'lider': lider})

    def update(request, id_lider):
        lider = Lideres.objects.get(pk=id_lider)
        form=FormularioLideres(request.POST, instance=lider)
        if form.is_valid():
            form.save()
        lideres = Lideres.objects.all()
        return render(request, "lideres_index.html", {"lideres": lideres})

    def delete(request, id_lider):
        lider = Lideres.objects.get(pk=id_lider)
        lider.delete()
        lideres = Lideres.objects.all()
        return render(request, "lideres_index.html", {"lideres": lideres})
