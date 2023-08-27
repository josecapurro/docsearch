from django.db import models

# Create your models here.

class SearchBackend(models.Model):
    name = models.CharField(max_length=130)
    description = models.CharField(max_length=130)
    host = models.CharField(max_length=130)
    port = models.CharField(max_length=130)
    user = models.CharField(max_length=130)
    password = models.CharField(max_length=130)
    active = models.BooleanField(default=False)
