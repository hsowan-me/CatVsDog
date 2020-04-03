from django.db import models


class Img(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)
