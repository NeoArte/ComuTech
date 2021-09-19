from django.contrib import admin
from .models import User


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'cpf', 'phone', 'cep', 'birth_date']
    list_display_links = ['id', 'name', 'email', 'cpf', 'phone', 'cep', 'birth_date']

admin.site.register(User, UsuarioAdmin)