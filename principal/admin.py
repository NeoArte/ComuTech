from django.contrib import admin
from .models import Usuario


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'cpf', 'telefone', 'cep', 'data_nascimento']