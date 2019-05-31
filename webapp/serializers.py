from rest_framework import serializers, viewsets
from django import forms
from . models import visitantes

class visitantesSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=visitantes
        fields = ('visitante','destino', 'entrada', 'salida')
        

class visitantesViewSet(viewsets.ModelViewSet):
    queryset = visitantes.objects.all()
    serializer_class = visitantesSerializer


