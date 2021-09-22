from django.db import models
from django.utils import timezone
import django.core.validators as validators
import datetime


class User(models.Model): # Usuários

    # Define um úsuario dentro da plataforma. Esse possui: nome, email, cpf (apenas números), telefone, cep (apenas números), 
    # data de nascimento (s/ horário, formato padrão é AAAA-MM-DD-hh-mm-ss-ms, Ano-Mês-Dia-Hora-Minuto-Segundo-Milisegundo), senha,
    # foto de perfil (salvo em MEDIA/usuarios/), whatsapp, data de criação e 3 campos não obrigátorios que são 
    # twitter (nome de úsuario sem o @), facebook (nome de perfil) e instagram (nome de úsuario)

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cpf = models.CharField(max_length=11, validators=[validators.MinLengthValidator(11)])
    phone = models.CharField(max_length=13)
    cep = models.CharField(max_length=8, validators=[validators.MinLengthValidator(8)])
    birth_date = models.DateField()
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='usuarios/', blank=True)

    whatsapp = models.CharField(max_length=13)
    twitter = models.CharField(blank=True, max_length=15, validators=[validators.MinLengthValidator(4)])
    facebook = models.CharField(blank=True, max_length=255)
    instagram = models.CharField(blank=True, max_length=30)

    creation_date = models.DateTimeField(default=timezone.now)

class AidType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

class Aid(models.Model): # Socorros

    # O socorro é a principal engrenagem da plataforma, ele necessita e apenas existe caso tenha um criador (usuário), necessita de um tipo, titulo, 
    # descrição (pode ficar em branco), data de criação, data_conclusão (por padrão estará em branco), estado (a letra de um dos estados em 'STATES') e
    # por fim os contribuidores que é uma relação de muitos para muitos com usuários (muitos usuarios podem ser contribuidores de muitos socorros)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="criador")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.ForeignKey(AidType, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now) # Quando o socorro foi aberto, usado para a "data de validade" dele
    ending_date = models.DateTimeField(blank=True) # Quando finalizado pelo úsuario entre em uma contagem para ser excluido.

    # Estados possiveis para um socorro, aberto enquanto no tempo de funcionamento,
    # congelado quando esse tempo acaba e finalizado quando o usuário finaliza aquele pedido.
    STATES = (("A", "Aberto"), ("C", "Congelado"), ("F", "Finalizado"))
    state = models.CharField(max_length=1, choices=STATES, default="A")

    # Contribuidores é "Muitos para Muitos" pois muitos socorros podem ser ajudos por muitos usuários diferentes.
    contributors = models.ManyToManyField(User, related_name="contribuidores")

class AidPhotos(models.Model):
    # Fotos usadas em um socorro, precisa estar associado a um socorro, conter uma imagem (salva em MEDIA/socorros/) e uma descrição usada em leitores de tela.

    aid = models.ForeignKey(Aid, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="socorros/", default="")
    description = models.TextField(blank=True) # Descrição na imagem para leitores de tela.

# class Time(models.Model):
    