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
