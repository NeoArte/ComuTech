from django.urls import path
from . import views

urlpatterns = [
  
    path("", views.home, name="home"), # Página Inicial - caso esteja logado redirecionar
    path("register/", views.register, name="register"), # Página de Registro
    
  
    path("login/", views.log_in, name="login"), # Página de Login 
    path("logout/", views.log_out, name="logout"),

  
    path("explore/", views.explore, name="explore"), # Página para Explorar
    path("explore/<int:pk>/", views.seeAid, name="visualizar"), # Abre um socorro de acordo com o ID (<int>) para o visualizar.

  
    path("user/<int:pk>/", views.user), # Página para visualizar informações da conta. O int é o ID DA CONTA
    path("user/<int:id>/edit/", views.edit_account),

  
    path("need-aid/", views.needAid, name="need_aid"), # Página para criação do socorro.
    path("need-aid/create-aid/", views.createAid), # Cria o o socorro e redireciona para "explorar/id_do_socorro" para visualiza-lo. O SEGUNDO INT é o id do socorro
    path("open/<int:pk>", views.openAid), # Descongela o Socorro que estava Congelado
    path("close/<int:pk>", views.closeAid), # Finaliza o socorro 
]