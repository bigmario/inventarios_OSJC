from django.contrib import admin
from .models import Alumno, Representante, Instrumento, Comodato

# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telf', 'email','nucleo', 'representante_id')
    list_filter = ('nombre', 'apellido', 'nucleo')

class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'ci', 'telf', 'email')
    list_filter = ('nombre', 'apellido')

class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ('serial', 'sin_fundamusical', 'nombre', 'marca','modelo', 'familia')
    list_filter = ('serial', 'nombre', 'familia')

class ComodatoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'instrumento_serial', 'alumno')
    list_filter = ('alumno', 'instrumento_serial', 'fecha')


admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Representante, RepresentanteAdmin)
admin.site.register(Instrumento, InstrumentoAdmin)
admin.site.register(Comodato, ComodatoAdmin )


