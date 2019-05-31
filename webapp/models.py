from django.db import models


class visitantes(models.Model):
    visitante = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    entrada = models.DateTimeField()
    salida = models.DateTimeField()
    
    def __str__(self):
        return self.visitante
    
