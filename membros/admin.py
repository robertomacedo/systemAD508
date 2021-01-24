from django.contrib import admin

from .models import CadMembro


@admin.register(CadMembro)
class Cad(admin.ModelAdmin):
    list_display = ("name", "cpf", "phone_namber")
