from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def quienessomos(request):
    return render(request, 'quienes_somos.html')

def equipo(request):
    return render(request, 'equipo.html')

def logros(request):
    return render(request, 'logros.html')

def formaparte(request):
    return render(request, 'forma_parte.html')

def acercaeat(request):
    return render(request, 'acerca_eat.html')

# AREAS

def quehacemos(request):
    return render(request, 'que_hacemos.html')

def cienciatecnologia(request):
    return render(request, 'ciencia_tecnologia.html')

def cooperacioninternacional(request):
    return render(request, 'cooperacion_internacional.html')

def desarrollolocal(request):
    return render(request, 'desarrollo_local.html')

def empresasemprendimientos(request):
    return render(request, 'empresas_emprendimientos.html')
