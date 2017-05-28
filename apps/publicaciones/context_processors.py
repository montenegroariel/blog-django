from .models import Publicacion


def publicaciones(request):
    context = Publicacion.objects.all()[:2]
    return {'ultimas_publicaciones': context}