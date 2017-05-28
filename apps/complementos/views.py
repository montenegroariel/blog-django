from django.http import JsonResponse
from django.core import serializers
from django.http import StreamingHttpResponse
from .models import Ciudad
# Create your views here.

def ciudades_ajax(request):
    ciudades = Ciudad.objects.filter(pais_id=request.POST.get('pais_id'))
    data = serializers.serialize('json', ciudades)
    return StreamingHttpResponse(data, content_type='application/json')

    #return JsonResponse({'ciudades': ciudades})