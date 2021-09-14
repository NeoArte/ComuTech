from django.db import models
from django.utils import timezone
import django.core.validators as validators
# import datetime

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cpf = models.IntegerField(max_length=11, validators=[validators.MinLengthValidator(11)]) # 11 números compõem um CPF, pode ser usado como primeiro campo de um login
    telefone = models.IntegerField(max_length=13)
    cep = models.IntegerField(max_length=8, validators=[validators.MinLengthValidator(8)])
    data_nascimento = models.DateTimeField() # Recbe um objeto datetime que conterá as informações da data. ex: dt = datetime(2015, 10, 09, 23, 55, 59, 25454...)
    senha = models.CharField(max_length=255)

    whatsapp = models.IntegerField(max_length=13)
    twitter = models.CharField(blank=True, max_length=15, validators=[validators.MinLengthValidator(4)]) # Isso se refere ao @ da pessoa, todavia o @ (character) não entra.
    facebook = models.CharField(blank=True)
    instagram = models.CharField(blank=True, max_length=30) # Isso se referece ao nome de úsuario (@), não o nome.

    data_criacao = models.DateTimeField(default=timezone.now)
