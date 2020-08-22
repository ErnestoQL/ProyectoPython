from django.db import models

# Create your models here.
class Lideres(models.Model):
    lider = models.CharField(max_length=50)

    def __str__(self):
        return self.lider