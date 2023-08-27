from django.db import models
from storagebackend.models import StorageBackend
from searchbackend.models import SearchBackend

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=130)
    description = models.CharField(max_length=130) 
    storagebackend = models.ForeignKey(StorageBackend, on_delete=models.CASCADE)
    storagebackend_user = models.CharField(max_length=130)
    storagebackend_password = models.CharField(max_length=130)
    searchbackend = models.ForeignKey(SearchBackend, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
