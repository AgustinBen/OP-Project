from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'bienvenido' : 'Bienvenido'
    }

    return render(request, 'template/index.html', context)