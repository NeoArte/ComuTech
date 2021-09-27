from django.urls import path
from . import views

urlpatterns = [

    #TODO - Trocar int por <int:variavel>| INT É APENAS PARA TESTES

    path("", views.index, name="index"), # Página Inicial - caso esteja logado redirecionar
    path("register/", views.register, name="register"), # Página de Registro
    
    path("login/", views.log_in, name="login"), # Página de Login 
    path("logout/", views.log_out, name="logout"),

    path("explorar/", views.explorar, name="explorar"), # Página para Explorar
    path("explorar/int/", views.visualizar, name="visualizar"), # Abre um socorro de acordo com o ID (<int>) para o visualizar.
    # path("search/", views.search, name="search"),

    #TODO - ao acessar apenas "usuario" redireciona para "usuario/int" da própria pessoa

    path("usuario/int/", views.usuario, name="usuario"), # Página para visualizar informações da conta. O int é o ID DA CONTA
    path("usuario/int/editar/", views.editarconta, name="editarconta"),
    
    path("usuario/int/socorrosmeus/", views.socorros_meus, name="socorrosmeus"), # Em "meus socorros" pode criar, editar, visualizar ou deletar um socorro
    path("criacao", views.criacao, name="criacao"), # Página para criação do socorro.
    path("criar/int", views.criar), # Cria o o socorro e redireciona para "explorar/id_do_socorro" para visualiza-lo. O SEGUNDO INT é o id do socorro
    path("deletar/<int:pk>", views.deletar) # Deleta o socorro e redireciona para "socorrosmeus"

]