from django.db import models

# Create your models here.

class StorageBackend(models.Model):
    STORAGE_S3 = 's3'
    STORAGE_SFTP = 'sftp'
    STORAGE_CHOICES = [
            (STORAGE_S3, 's3'),
            (STORAGE_SFTP, 'sftp'),
            ]
    name = models.CharField(max_length=130)
    description = models.CharField(max_length=130)
    kind = models.CharField(max_length=130, choices=STORAGE_CHOICES)
    url = models.CharField(max_length=130)
    active = models.BooleanField(default=False)
