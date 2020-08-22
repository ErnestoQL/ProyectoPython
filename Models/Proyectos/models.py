from django.db import models
from Models.Lideres.models import Lideres
from Models.Categorias.models import Categorias


class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    fecha = models.DateField()
    programadores = models.CharField(max_length=50)
    computadoras = models.CharField(max_length=50)
    estatus = models.CharField(max_length=50)
    lider_idLider = models.ForeignKey(Lideres, on_delete=models.CASCADE)
    categoria_idCategoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    def __str__(self):
            return self.id_inscripcion