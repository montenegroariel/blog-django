from django.views.generic import ListView, DetailView
from .models import Publicacion


class CategoriaListView(ListView):
    model = Publicacion
    paginate_by = 5

    def get_queryset(self):
        qs = super(CategoriaListView, self).get_queryset()
        return qs.filter(categoria__nombre=self.kwargs['nombre'])


class PublicacionListView(ListView):
    model = Publicacion
    paginate_by = 5

    def get_queryset(self):
        query = super(PublicacionListView, self).get_queryset()
        if 'buscar' in self.request.GET:
            query = Publicacion.objects.filter(titulo__icontains=self.request.GET['buscar'])
        return query


class PublicacionDetailView(DetailView):
    model = Publicacion

    def get_object(self):
        object = super(PublicacionDetailView, self).get_object()
        object.visitas += 1
        object.save()
        return object
