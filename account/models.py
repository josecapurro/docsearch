from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
