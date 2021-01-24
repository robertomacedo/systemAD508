from django.contrib import admin

from .models import CadMembro, Documento


@admin.register(CadMembro)
class Cad(admin.ModelAdmin):
    list_display = ("name", "phone_number", "created", "updated")

@admin.register(Documento)
class Doc(admin.ModelAdmin):
    list_display = ("cpf", "rg", "created", "updated")