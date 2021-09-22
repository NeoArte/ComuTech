from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .form import RegistrationForm

is_logged_in = False

# As funções com testes "if_logged_in" verificam se o usuário está logado, se estiver acessa a página normalmente e 
# caso contrário é redirecionado para a página de login (determinadno que é necessário estar logado), as páginas com apenas redirects são as que fazem
# ações HTTP (ex: POST) e devolvem o úsuario para alguma tela, geralmente a anterior.

def index(request):
    return render(request, "principal/index.html")

def cadastro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Registrado')
            return redirect('index')

    form = RegistrationForm() 
    context = {
        'form': form,
    }
    return render(request, "principal/cadastro-customuser.html", context)

def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        print("\n\n\n", email, " : ", password, "\n=====\n", user,  "\n\n\n")
        if user is not None:
            print("\n\nLOGADO\n\n")
            login(request, user)
            return redirect('index')
        else:
            print("\n\nERRO\n\n")
            return redirect('cadastro')
    return render(request, "principal/login-customuser.html")

def process_login(request):
    return redirect('index')


def explorar(request):
    return render(request, "principal/explorar.html")

def visualizar(request):

    return render(request, "principal/socorro.html")

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

def socorros_meus(request):
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

def deletar(request):
    if is_logged_in:
        # Apenas fazer a ação de deletar aqui dentro.
        return redirect('socorrosmeus')
    elif not is_logged_in:
        return redirect('login')
