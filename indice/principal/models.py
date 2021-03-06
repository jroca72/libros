from django.db import models
from datetime import datetime

# Create your models here.

class autores(models.Model): 
    autor = models.CharField(max_length=75) 
    
    def __unicode__(self):
    	return self.autor
    	
class libros(models.Model): 
    titulo = models.CharField(max_length=85) 
    autor = models.ForeignKey(autores, default=None, null=False, blank=False)
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    puntuacion = models.PositiveIntegerField(default=1, null=False, blank=False) 
    isbn = models.CharField(max_length=50, default=0)     
    
    def __unicode__(self):
    	return self.titulo
