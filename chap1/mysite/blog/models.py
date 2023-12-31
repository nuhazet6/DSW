from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # Si añadimos primary key a un campo del modelo django no genera el campo id
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    title = models.CharField(max_length=250, primary_key=True)
    slug = models.SlugField(max_length=250)
    body = models.TextField()  # Dont need max_length like CharField or SlugField
    publish = models.DateTimeField(
        default=timezone.now
    )  # Como se relaciona el status con el timezone.now? si no se relacionan como se llega a la hora de publicación?
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )  # Cuidado con añadir campos ForeignKey y Not Null después de hacer makemigrations

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        '''
        Important method, this is the default Python method to return a string with
        the human-readable representation of the object. Django will use this method
        to display the name of the object in many places.
        '''
        return self.title
