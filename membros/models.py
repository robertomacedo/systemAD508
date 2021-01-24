from django.contrib.auth.models import User
from django.db import models


class CadMembro(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_namber = models.CharField(max_length=30)
    conjuge = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

