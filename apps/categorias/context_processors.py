from .models import Categoria


def categorias(request):
    context = Categoria.objects.all()
    return {'categorias': context}