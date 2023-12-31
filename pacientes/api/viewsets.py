from rest_framework import viewsets
from pacientes.api import serializers
from pacientes import models

class pacientesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PacientesSerializer
    queryset = models.Pacientes.objects.all()
