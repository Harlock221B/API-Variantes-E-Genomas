from django.db import models
from uuid import uuid4

class Variante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cromossomo = models.CharField(max_length=255)
    posicao = models.IntegerField()
    base_referencia = models.CharField(max_length=10,default='A',choices=(('A','A'),('T','T'),('C','C'),('G','G')))
    base_alternativa = models.CharField(max_length=10,default='A',choices=(('A','A'),('T','T'),('C','C'),('G','G')))

    class Meta:
        verbose_name = "Variante genética"
        verbose_name_plural = "Variantes genéticas"

    def __str__(self):
        return f"{self.cromossomo}:{self.posicao}{self.base_referencia}>{self.base_alternativa}"

