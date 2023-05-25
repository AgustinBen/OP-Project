from django import forms
from .models import  Pregunta, Respuesta, preguntasRespondidas



class cantidadCorrectas(forms.BaseInlineFormSet):
    def clean(self):
        super(cantidadCorrectas, self).clean()

        respuestaCorrecta = 0

        for formulario in self.forms:
            if not formulario.is_valid():
                return
            
            if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
                respuestaCorrecta += 1

        try:
            assert respuestaCorrecta == Respuesta.respuestasPermitidas 
        
        except AssertionError:
            raise forms.ValidationError('Seleccionar una sola respuesta correcta!')
