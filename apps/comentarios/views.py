from django.views.generic import CreateView

from .models import Comentario
from .forms import ComentarioForm
from apps.publicaciones.models import Publicacion


class ComentarioCreateView(CreateView):
    model = Comentario
    form_class = ComentarioForm
    success_url = '/publicaciones'

    def get_context_data(self, **kwargs):
        context = super(ComentarioCreateView, self).get_context_data(**kwargs)
        context['publicacion'] = Publicacion.objects.get(slug=self.kwargs['slug'])
        return context