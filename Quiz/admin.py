from django.contrib import admin
from .models import Pregunta, Respuesta, preguntasRespondidas
from .forms import cantidadCorrectas

# Register your models here.

class elegirRespuesta(admin.TabularInline):
    model = Respuesta
    formset = cantidadCorrectas


class preguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (elegirRespuesta, )
    list_display = ['texto',]
    search_fields = ['texto', 'preguntas__texto']


class pregRespAdmin(admin.ModelAdmin):
    list_display = ['pregunta','respuesta', 'correcta', 'puntaje']

    class Meta:
        model = preguntasRespondidas



admin.site.register(preguntasRespondidas)
admin.site.register(Pregunta, preguntaAdmin)
admin.site.register(Respuesta)