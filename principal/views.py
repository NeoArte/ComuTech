from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

is_logged_in = False

# As funções com testes "if_logged_in" verificam se o usuário está logado, se estiver acessa a página normalmente e 
# caso contrário é redirecionado para a página de login (determinadno que é necessário estar logado), as páginas com apenas redirects são as que fazem
# ações HTTP (ex: POST) e devolvem o úsuario para alguma tela, geralmente a anterior.

def index(request):
    return render(request, "principal/index.html")

def cadastro(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, "principal/cadastro.html", context)

def login(request):
    return render(request, "principal/login.html")

def explorar(request):
    return render(request, "principal/explorar.html")

def visualizar(request):

    return render(request, "principal/index.html")

def usuario(request):
    if is_logged_in:
        return render(request, "principal/usuario.html")
    elif not is_logged_in:
        return redirect('login')

def editarconta(request):
    if is_logged_in:
        return render(request, "principal/editarconta.html")
    elif not is_logged_in:
        return redirect('login')

def socorrosmeus(request):
    if is_logged_in:
        return render(request, "principal/socorrosmeus.html")
    elif not is_logged_in:
        return redirect('login')

def criacao(request):
    if is_logged_in:
        return render(request, "principal/criacao.html")
    elif not is_logged_in:
        return redirect('login')

def criar(request):
    return redirect('socorrosmeus')

def editar(request):
    if is_logged_in:
        return render(request, "principal/criacao.html") #Usa o html de criação, mas iremos carregar as informações junto
    elif not is_logged_in:
        return redirect('login')

def atualizar(request):
    if is_logged_in:
        # Apenas fazer a ação de atualizar aqui dentro.
        return redirect('socorrosmeus')
    elif not is_logged_in:
        return redirect('login')

def deletar(request):
    if is_logged_in:
        # Apenas fazer a ação de deletar aqui dentro.
        return redirect('socorrosmeus')
    elif not is_logged_in:
        return redirect('login')
