from django import forms
from captcha.fields import CaptchaField

class ContactoForm(forms.Form):
    nombre = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    mail = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    mensaje = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    captcha = CaptchaField()