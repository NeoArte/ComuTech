from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.http import request
from django.utils import timezone
import django.core.validators as validators
import datetime


# Classes ligadas ao usuário (User related classes) ===================

# User Manager é a classe responsável por lidar com o que ocorre durante a criação de um usuario (create_user) e super usuario (create_super_user)
class UserManager(BaseUserManager):
    def create_user(
        self, cpf, name, email, phone, country, state, city, neighborhood, street, house_number, add_info, cep, birth_date, 
        facebook, whatsapp, instagram, twitter, profile_picture, password=None,):
        
        if not cpf: 
            raise ValueError("Usuários precisam ter um CPF - Users must have a CPF")
        
        if not name:
            raise ValueError("Usuários precisam ter um nome - Users must have a name")

        if not email:
            raise ValueError("Usuários precisam ter um endereço de email - Users must have an email adress")

        if not phone:
            raise ValueError("Usuários precisam ter um número de celular - Users must have a phone number")

        if not country:
            raise ValueError("Usuários precisam ter um pais - Users must have a country")
        if not state:
            raise ValueError("Usuários precisam ter um estado - Users must have a state")
        if not city:
            raise ValueError("Usuários precisam ter uma city - Users must have a city")
        if not neighborhood:
            raise ValueError("Usuários precisam ter um bairro - Users must have a neighborhood")
        if not street:
            raise ValueError("Usuários precisam ter uma rua - Users must have a street")
        if not house_number:
            raise ValueError("Usuários precisam ter um número de casa - Users must have a house number")
        if not cep:
            raise ValueError("Usuários precisam ter um CEP - Users must have a CEP")

        if not birth_date:
            raise ValueError("Usuários precisam ter um CEP - Users must have a birth date")


        user = self.model(
            cpf=cpf,
            name=name,
            email=self.normalize_email(email), # Normalize -> deixa tudo em letra minúscula
            phone=phone,
            country=country,
            state=state,
            city=city,
            neighborhood=neighborhood,
            street=street,
            house_number=house_number,
            add_info=add_info,
            cep=cep,
            birth_date=birth_date,
            facebook=facebook,
            whatsapp=whatsapp,
            instagram=instagram,
            twitter=twitter,
            profile_picture=profile_picture,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(
        self, cpf, name, email, phone, country, state, city, neighborhood, street, house_number, add_info, cep, birth_date, 
        facebook, whatsapp, instagram, twitter, profile_picture, password):
        user = self.create_user(
            cpf=cpf,
            name=name,
            email=self.normalize_email(email), # Normalize -> deixa tudo em letra minúscula
            phone=phone,
            country=country,
            state=state,
            city=city,
            neighborhood=neighborhood,
            street=street,
            house_number=house_number,
            add_info=add_info,
            cep=cep,
            birth_date=birth_date,
            password=password,
            facebook=facebook,
            whatsapp=whatsapp,
            instagram=instagram,
            twitter=twitter,
            profile_picture=profile_picture,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser): # Usuários

    # Define um úsuario dentro da plataforma. Esse possui: nome, email, cpf (apenas números), telefone, um conjunto de campos para localização descritos abaixo, 
    # data de nascimento (s/ horário, formato padrão é AAAA-MM-DD-hh-mm-ss-ms, Ano-Mês-Dia-Hora-Minuto-Segundo-Milisegundo), senha,
    # foto de perfil (salvo em MEDIA/usuarios/), whatsapp, data de criação e 3 campos não obrigátorios que são 
    # twitter (nome de úsuario sem o @), facebook (nome de perfil) e instagram (nome de úsuario)

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    cpf = models.CharField(max_length=11, validators=[validators.MinLengthValidator(11)], unique=True)
    phone = models.CharField(max_length=13)

    # Campos ligados a localização, traduzindo se tratam respectivamente de:
    # País - Estado - Cidade - Bairro - Número da casa (ou prédio) - Informações adicionais (como o número do apartamento) - CEP
    
    country = models.CharField(max_length=255, default="")
    state = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="")
    neighborhood = models.CharField(max_length=255, default="")
    street = models.CharField(max_length=255, default="")
    house_number = models.CharField(max_length=255, default="")
    add_info = models.CharField(max_length=255, blank=True, null=True, default="")
    cep = models.CharField(max_length=8, validators=[validators.MinLengthValidator(8)])

    birth_date = models.DateField()
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='users/', default='users/empty-img-profile.jpg')

    whatsapp = models.CharField(max_length=13, null=True, blank=True)
    twitter = models.CharField(null=True, blank=True, max_length=15, validators=[validators.MinLengthValidator(4)])
    facebook = models.CharField(null=True, blank=True, max_length=255)
    instagram = models.CharField(null=True, blank=True, max_length=30)


    # OBRIGADO pelo Django (REQUIRED by Django)

    date_joined = models.DateTimeField(auto_now_add=timezone.now, verbose_name="date joined")
    last_login = models.DateTimeField(auto_now=True, verbose_name="last login")
    is_admin = models.BooleanField(default=False) # É admin?
    is_active = models.BooleanField(default=True) # Está ativo?
    is_staff = models.BooleanField(default=False) # É da equipe (quem trabalha)?
    is_superuser = models.BooleanField(default=False) # É um super usuário (privilégios especiais)

    USERNAME_FIELD = 'email' # O que será usado para realizar o login
    REQUIRED_FIELDS = [
        'name', 'cpf', 'phone', 'country', 'state', 'city', 'neighborhood', 'street', 'house_number', 'add_info', 'cep', 'birth_date', 
        'whatsapp', 'twitter', 'facebook', 'instagram', 'profile_picture']

    objects = UserManager()

    # O que retornar ao dar print em User
    def __str__(self):
        return self.name + ":" + self.email+ ":" + self.cpf
        
    # Retorna se o usuario tem permissão (é admin)
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


# Classes Comuns (Common Classes) ========================

class AidType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Aid(models.Model): # Socorros

    # O socorro é a principal engrenagem da plataforma, ele necessita e apenas existe caso tenha um criador (usuário), necessita de um tipo, titulo, 
    # descrição (pode ficar em branco), data de criação, data_conclusão (por padrão estará em branco), estado (a letra de um dos estados em 'STATES') e
    # por fim os contribuidores que é uma relação de muitos para muitos com usuários (muitos usuarios podem ser contribuidores de muitos socorros)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="myaid")
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey(AidType, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now) # Quando o socorro foi aberto, usado para a "data de validade" dele
    ending_date = models.DateTimeField(null=True, blank=True) # Quando finalizado pelo úsuario entre em uma contagem para ser excluido.

    # Estados possiveis para um socorro, aberto enquanto no tempo de funcionamento,
    # congelado quando esse tempo acaba e finalizado quando o usuário finaliza aquele pedido.
    STATES = (("A", "Aberto"), ("C", "Congelado"), ("F", "Finalizado"))
    state = models.CharField(max_length=1, choices=STATES, default="A")


class AidPhotos(models.Model):
    # Fotos usadas em um socorro, precisa estar associado a um socorro, conter uma imagem (salva em MEDIA/socorros/) e uma descrição usada em leitores de tela.

    aid = models.ForeignKey(Aid, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="socorros/", default="")
    description = models.TextField(null=True, blank=True) # Descrição na imagem para leitores de tela.
