from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    PrimerNombre = models.CharField(max_length=25)
    SegundoNombre = models.CharField(max_length=25)
    PrimerApellido = models.CharField(max_length=25)
    SegundoApellido = models.CharField(max_length=25)
    Edad = models.CharField(max_length=2)
    created_date = models.DateTimeField(
            default=timezone.now)
    PhotoPerfil = models.ImageField(upload_to='photos')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title