from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.core.mail import send_mail

from .forms import ContactoForm


class ContactoView(FormView):
    template_name = 'contactos/contacto_form.html'
    form_class = ContactoForm
    success_url = '/contactos/gracias/'

    def form_valid(self, form):

        nombre = form.cleaned_data['nombre']
        mail = form.cleaned_data['mail']
        mensaje = 'Este mail fue enviado desde el sitio web.\n \n' + \
                  'Nombre: ' + nombre + '\n' + \
                  'Mail: ' + mail + '\n \n' + \
                  form.cleaned_data['mensaje']
        send_mail(nombre, mensaje , 'contacto@capymef.org.ar', ['presidencia@capymef.org.ar'])
        return super(ContactoView, self).form_valid(form)


class ContactoTemplateView(TemplateView):
    template_name = 'contactos/gracias.html'