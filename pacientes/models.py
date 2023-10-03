from django.db import models
from variantes.models import Variante
from uuid import uuid4

class Pacientes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    idade = models.IntegerField()
    variantes = models.ManyToManyField(
        "variantes.Variante", related_name="pacientes"
    )
    
    def __str__(self):
        return f"{self.nome} variante(s): {self.variantes.count()}"