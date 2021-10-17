from django.contrib import admin
from .models import Review, Aid, AidType, User


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'cpf', 'phone', 'cep', 'birth_date', 'whatsapp', 'facebook', 'instagram', 'twitter', 'profile_picture']
    list_display_links = ['id', 'name', 'email', 'cpf', 'phone', 'cep', 'birth_date']

class AidTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_display_links = ['id', 'name', 'description']

class AidAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'description', 'type', 'creation_date', 'ending_date', 'state']
    list_display_links = ['id', 'title', 'description']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'aid', 'result', 'rating', 'feedback']
    list_display_links = ['id', 'aid']

admin.site.register(AidType, AidTypeAdmin)
admin.site.register(User, UsuarioAdmin)
admin.site.register(Aid, AidAdmin)
admin.site.register(Review, ReviewAdmin)