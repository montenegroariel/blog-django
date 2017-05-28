from django.db import models


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=1000)



    def __str__(self):
       return str(self.mail)
