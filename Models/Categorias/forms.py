from django import forms

from Models.Categorias.models import Categorias


class FormularioCategorias(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'