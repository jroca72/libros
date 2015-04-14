from django.shortcuts import render

from principal.models import libros

# Create your views here.

def indice(request):
	los_libros = libros.objects.all().order_by('-fecha')
	context = {'los_libros': los_libros }
	return render(request, 'principal/index.html', context)
