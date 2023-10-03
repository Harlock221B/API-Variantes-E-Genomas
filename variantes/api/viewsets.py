from rest_framework import viewsets
from variantes.api import serializers
from variantes import models

class variantesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VariantesSerializer
    queryset = models.Variante.objects.all()