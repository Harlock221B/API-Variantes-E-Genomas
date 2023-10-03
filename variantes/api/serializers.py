from rest_framework import serializers
from variantes import models

class VariantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Variante
        fields = "__all__"