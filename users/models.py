from django.db import models

# my imports
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

