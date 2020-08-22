from django import forms

from Models.Lideres.models import Lideres


class FormularioLideres(forms.ModelForm):
    class Meta:
        model = Lideres
        fields = '__all__'