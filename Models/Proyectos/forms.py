from django.forms import ModelForm
from django.forms import  DateInput

from Models.Proyectos.models import Proyectos


class formularioProyectos(ModelForm):
    class Meta:
        model = Proyectos
        fields = [
            'lider_idLider',
            'categoria_idCategoria',
            'programadores',
            'computadoras',
            'estatus',
            'fecha',

        ]
        labels = {
            'lider_idLider': 'Lider',
            'categoria_idCategoria': 'Categoria',
            'programadores': 'Programadores',
            'computadoras': 'Computadoras',
            'estatus': 'Estatus',
            'fecha':'Fecha de Creacion',

        }

        widgets = {"fecha": DateInput(attrs={'type': 'date'})}