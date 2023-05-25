from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class Pregunta(models.Model):

    texto = models.TextField(verbose_name='Texto de la pregunta')

    def __str__(self):
        return self.texto
    

class Respuesta(models.Model):
    
    respuestasPermitidas = 1

    pregunta = models.ForeignKey(Pregunta, related_name='preguntas', on_delete=models.CASCADE)
    correcta = models.BooleanField(verbose_name='es la correcta?', default=False, null=False)
    texto = models.TextField(verbose_name='texto de la respuesta')

    def __str__(self):
        return self.texto
    

class preguntasRespondidas(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE, related_name='intentos')
    correcta = models.BooleanField(verbose_name='Es esta la respuesta correcta?', default=False, null=False)
    puntaje = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=6)



class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntajeTotal = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)