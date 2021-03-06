from django.db import models
from django.urls import reverse
# Create your models here.
import uuid  # para no usar id en la URL
from django.contrib.auth import get_user_model


class Book(models.Model):
    # modificamos el ID para que sea UUID, el UUID4
    # es para encriptacion

    # si borramos tambien esto de id= podemos hacer como hacimamos antes
    # en las url, osea:
    # path('<int:pk>', BookDetailView.as_view(), name='book_detail'),
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    class Meta:
        # para agregar Index a las tablas de BD y aumentar la velocidad
        # a costa de ocupar mas espacio obviamente
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]
        permissions = [
            ('special_status', 'Can read all books'),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('book_detail', args=[str(self.id)])


class Review(models.Model):  # new
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review
