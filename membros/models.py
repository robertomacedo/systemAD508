from django.contrib.auth.models import User
from django.db import models


class CadMembro(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    conjuge = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Documento(models.Model):
    cpf = models.CharField(max_length=20)
    rg = models.CharField(max_length=20)
    titulo = models.CharField(max_length=20)
    cnh = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
