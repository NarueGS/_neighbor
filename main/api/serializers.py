from dataclasses import fields
from rest_framework import serializers
from main import models

class InquilinosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inquilinos
        fields = '__all__'

class UnidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Unidades
        fields = '__all__'

class Despesas_UnidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Despesas_Unidades
        fields = '__all__'