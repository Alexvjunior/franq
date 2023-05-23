from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    interest = models.BooleanField(max_length=255)
