from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from rest_framework import generics
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
#from rest_framework.response import Response
from rest_framework import status
from . models import visitantes
from webapp import serializers
from . serializers import visitantesSerializer
from django.db.models.query import QuerySet


class visitantesList(generics.ListCreateAPIView):
    queryset = visitantes.objects.all()
    serializer_class = visitantesSerializer
    def get_object(self):
        queryset =self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk']
        )
        return obj
        
    #def get(self, request):
    #    visitantes1 = visitantes.objects.all()
    #    serializer = visitantesSerializer(visitantes1, many=True)
    #    return Response(serializer.data)
    
    
    #def post(self):
    #    pass
    
def lista_visitantes(request):
    visitas = visitantes.objects.all()
    return render(request, 'Registros2.html', {'visitas' : visitas})

def busqueda(request):
    if 'q' in request.GET:
        q = request.GET['q']
        message = 'You searched for: %r' % request.GET['q']
        visitas = visitantes.objects.filter(visitante__icontains = q)
        
    else:
        message = 'You submitted an empty form.'
    return render(request, 'Registros.html', {'message': message, 'visitas':visitas})

