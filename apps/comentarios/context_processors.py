from .models import Comentario


def comentarios(request):
    context = Comentario.objects.all()[:3]
    return {'ultimos_comentarios': context}