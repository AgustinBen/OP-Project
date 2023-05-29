from django.shortcuts import render, redirect
from .forms import RegistroFormulario

# Create your views here.

def index(request):
    context = {
        'bienvenido' : 'Bienvenido'
    }

    return render(request, 'template/index.html', context)


def registro(request):
    titulo = "Crea tu usuario"

    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = RegistroFormulario()

    context = {

        'form': form,
        'titulo': titulo,
    }

    return render(request, 'template/Usuario/registro.html', context)