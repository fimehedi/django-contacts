from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    info = models.CharField(max_length=30)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date = models.DateField(auto_now_add=True)
    manager = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def delete(self, *args, **kwargs):
        self.image.delete()
        return super().delete(*args, **kwargs)

    class Meta:
        ordering = ['-id']