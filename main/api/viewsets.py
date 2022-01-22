from rest_framework import viewsets
from main.api import serializers
from main import models

class InquilinosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.InquilinosSerializer
    queryset = models.Inquilinos.objects.all()

class UnidadesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UnidadesSerializer
    queryset = models.Unidades.objects.all()

class Despesas_UnidadesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Despesas_UnidadesSerializer
    queryset = models.Despesas_Unidades.objects.all()