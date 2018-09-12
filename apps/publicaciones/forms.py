from django import forms
from .models import Publicacion, Documento, Imagen
from suit_ckeditor.widgets import CKEditorWidget

class PublicacionForm(forms.ModelForm):
    #encabezado = forms.CharField(widget=CKEditorWidget(editor_options={'startupFocus': True}))
    #contenido = forms.CharField(widget=CKEditorWidget(editor_options={'startupFocus': True}))

    class Meta:
        model = Publicacion
        fields = '__all__'
        widgets = {
            'encabezado': CKEditorWidget(editor_options={'startupFocus': True}),
            'contenido': CKEditorWidget(editor_options={'startupFocus': True})

        }

    class Media:
        js = ('filebrowser/js/FB_CKEditor.js', 'filebrowser/js/FB_Redactor.js')
        css = {
            'all': ('filebrowser/css/suit-filebrowser.css',)
        }


class DocumentoForm(forms.ModelForm):
    documento = forms.FileField(
        label='Seleccione un archivo',
        help_text='max. 42 megabytes'
    )

    class Meta:
        model = Documento
        fields = '__all__'


class ImagenForm(forms.ModelForm):
    imagen = forms.FileField(
        label='Seleccione un archivo',
        help_text='max. 42 megabytes'
    )

    class Meta:
        model = Imagen
        fields = '__all__'