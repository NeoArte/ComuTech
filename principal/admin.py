from django.contrib import admin
from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'cpf', 'telefone', 'cep', 'data_nascimento']
    list_display_links = ['id', 'nome', 'email', 'cpf', 'telefone', 'cep', 'data_nascimento']

admin.site.register(Usuario, UsuarioAdmin)