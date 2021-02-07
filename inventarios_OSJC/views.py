from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola, Bienvenido al HOME del proyecto")