from django.db import models
from django.utils import timezone
import django.core.validators as validators
# import datetime

class Usuario(models.Model):

    # Define um úsuario dentro da plataforma. Esse possui: nome, email, cpf (apenas números), telefone, cep (apenas números), 
    # data de nascimento (s/ horário, formato padrão é AAAA-MM-DD-hh-mm-ss-ms, Ano-Mês-Dia-Hora-Minuto-Segundo-Milisegundo), senha,
    # foto de perfil (salvo em MEDIA/usuarios/), whatsapp, data de criação e 3 campos não obrigátorios que são 
    # twitter (nome de úsuario sem o @), facebook (nome de perfil) e instagram (nome de úsuario)

    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cpf = models.CharField(max_length=11, validators=[validators.MinLengthValidator(11)])
    telefone = models.CharField(max_length=13)
    cep = models.CharField(max_length=8, validators=[validators.MinLengthValidator(8)])
    data_nascimento = models.DateField()
    senha = models.CharField(max_length=255)
    foto_perfil = models.ImageField(upload_to='usuarios/', blank=True)

    whatsapp = models.CharField(max_length=13)
    twitter = models.CharField(blank=True, max_length=15, validators=[validators.MinLengthValidator(4)])
    facebook = models.CharField(blank=True, max_length=255)
    instagram = models.CharField(blank=True, max_length=30)

    data_criacao = models.DateTimeField(default=timezone.now)

class TipoSocorro(models.Model):
    # Tipos que socorros podem ter. A descrição é opcional, mas poderia ser útil para quando o usuário quisesse saber do que se trata aquela categoria.
    nome = models.ForeignKey
    descricao = models.TextField(blank=True) # Pode ser útil disponibilizar uma descrição para aquela categoria.

class Socorro(models.Model):

    # O socorro é a principal engrenagem da plataforma, ele necessita e apenas existe caso tenha um criador (usuário), necessita de um tipo, titulo, 
    # descrição (pode ficar em branco), data de criação, data_conclusão (por padrão estará em branco), estado (a letra de um dos estados em 'STATES') e
    # por fim os contribuidores que é uma relação de muitos para muitos com usuários (muitos usuarios podem ser contribuidores de muitos socorros)

    criador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="criador")
    tipo = models.ForeignKey(TipoSocorro, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    data_criacao = models.DateTimeField(default=timezone.now) # Quando o socorro foi aberto, usado para a "data de validade" dele
    data_conclusao = models.DateTimeField(blank=True) # Quando finalizado pelo úsuario entre em uma contagem para ser excluido.

    # Estados possiveis para um socorro, aberto enquanto no tempo de funcionamento,
    # congelado quando esse tempo acaba e finalizado quando o usuário finaliza aquele pedido.
    STATES = (("A", "Aberto"), ("C", "Congelado"), ("F", "Finalizado"))
    estado = models.CharField(max_length=1, choices=STATES, default="A")

    # Contribuidores é "Muitos para Muitos" pois muitos socorros podem ser ajudos por muitos usuários diferentes.
    contribuidores = models.ManyToManyField(Usuario, related_name="contribuidores")

class Fotos(models.Model):
    # Fotos usadas em um socorro, precisa estar associado a um socorro, conter uma imagem (salva em MEDIA/socorros/) e uma descrição usada em leitores de tela.

    socorro = models.ForeignKey(Socorro, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="socorros/", default="")
    descricao = models.TextField(blank=True) # Descrição na imagem para leitores de tela.


