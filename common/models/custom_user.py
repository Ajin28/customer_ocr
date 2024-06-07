from django.contrib.auth.models import AbstractUser
from common.models import Country
from django.db import models

class CustomUser(AbstractUser):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)