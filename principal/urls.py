from django.urls import path
from . import views

urlpatterns = [

    #TODO - Trocar int por <int:variavel>| INT É APENAS PARA TESTES

    path("", views.index, name="index"), # Página Inicial - caso esteja logado redirecionar
    path("cadastro/", views.cadastro, name="cadastro"), # Página de Registro
    path("login/", views.login, name="login"), # Página de Login 


    path("explorar/", views.explorar, name="explorar"), # Página para Explorar
    path("explorar/int/", views.visualizar, name="visualizar"), # Abre um socorro de acordo com o ID (<int>), visualiza ele.


    path("usuario/int/", views.usuario, name="usuario"), #Página para visualizar informações da conta. O int é o ID DA CONTA
    path("usuario/int/editar/", views.editarconta, name="editarconta"),

    path("usuario/int/socorrosmeus/", views.socorrosmeus, name="socorrosmeus"), # Em "meus socorros" pode criar, editar, visualizar ou deletar um socorro
    path("usuario/int/criacao", views.criacao, name="criacao"), # Página para criação do socorro.
    path("usuario/int/criar/int", views.criar), # Cria o o socorro e redireciona para "explorar/id_do_socorro" para visualiza-lo. O SEGUNDO INT é o id do socorro
    path("usuario/int/editar/int", views.editar, name="editar"), # Carrega as informações do socorro selecionado e permite editar
    path("usuario/int/atualizar/int", views.atualizar, name="atualizar"), # Atualiza o socorro após ser editado e redireciona para 'socorrosmeus'
    path("usuario/int/deletar/int", views.deletar) # Deleta o socorro e redireciona para "socorrosmeus"

]