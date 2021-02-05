from django.db import models
from django.urls import reverse
# Create your models here.
import uuid  # para no usar id en la URL


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

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('book_detail', args=[str(self.id)])
