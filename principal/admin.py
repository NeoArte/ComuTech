from django.contrib import admin
from .models import Aid, AidType, User


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'cpf', 'phone', 'cep', 'birth_date', 'whatsapp', 'facebook', 'instagram', 'twitter', 'profile_picture']
    list_display_links = ['id', 'name', 'email', 'cpf', 'phone', 'cep', 'birth_date']

class AidTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_display_links = ['id', 'name', 'description']

admin.site.register(AidType, AidTypeAdmin)
admin.site.register(User, UsuarioAdmin)