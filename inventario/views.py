from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio_inventario(request):
    return HttpResponse('Hola, Bienvenido a la seccion de inventarios!!')

def inicio_comodatos(request):
    return HttpResponse('Hola, Bienvenido a la seccion de comodatos!!')
