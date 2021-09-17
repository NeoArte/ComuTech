from django.db import models
from django.utils import timezone
import django.core.validators as validators
# import datetime

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cpf = models.CharField(max_length=11, validators=[validators.MinLengthValidator(11)]) # 11 números compõem um CPF, pode ser usado como primeiro campo de um login
    telefone = models.CharField(max_length=13)
    cep = models.CharField(max_length=8, validators=[validators.MinLengthValidator(8)])
    data_nascimento = models.DateField() # Recbe um objeto datetime que conterá as informações da data. ex: dt = datetime(2015, 10, 09, 23, 55, 59, 25454...)
    senha = models.CharField(max_length=255)
    foto_perfil = models.ImageField(upload_to='usuarios/', blank=True)

    whatsapp = models.CharField(max_length=13)
    twitter = models.CharField(blank=True, max_length=15, validators=[validators.MinLengthValidator(4)]) # Isso se refere ao @ da pessoa, todavia o @ (character) não entra.
    facebook = models.CharField(blank=True, max_length=255)
    instagram = models.CharField(blank=True, max_length=30) # Isso se referece ao nome de úsuario (@), não o nome.

    data_criacao = models.DateTimeField(default=timezone.now)

class TipoSocorro(models.Model):
    nome = models.ForeignKey
    descricao = models.TextField(blank=True) # Pode ser útil disponibilizar uma descrição para aquela categoria.

class Socorro(models.Model):
    criador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="criador") # Existe apenas se estiver associado a um úsuario
    tipo = models.ForeignKey(TipoSocorro, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now) # Quando o socorro foi aberto, usado para a "data de validade" dele
    data_conclusao = models.DateTimeField(blank=True) # Quando finalizado pelo úsuario entre em uma contagem para ser excluido.

    # Estados possiveis para um socorro, aberto enquanto no tempo de funcionamento,
    # congelado quando esse tempo acaba e finalizado quando o usuário finaliza aquele pedido.
    STATES = (("A", "Aberto"), ("C", "Congelado"), ("F", "Finalizado"))
    estado = models.CharField(max_length=1, choices=STATES, default="A")

    # Contribuidores é "Muitos para Muitos" pois muitos socorros podem ser ajudos por muitos usuários diferentes.
    contribuidores = models.ManyToManyField(Usuario, related_name="contribuidores")

class Necessidades(models.Model):
    socorro = models.ForeignKey(Socorro, on_delete=models.CASCADE) # Necessidades são parte de socorros (um socorro para muitas nec.)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    STATES = (("NF", "Não Finalizado"), ("F", "Finalizado")) # O status define se aquela necessidade foi cumprida
    estado = models.CharField(max_length=2, choices=STATES, default="NF")

class Fotos(models.Model):
    socorro = models.ForeignKey(Socorro, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="socorros/", default="")
    descricao = models.TextField(blank=True) # Descrição na imagem para leitores de tela.


