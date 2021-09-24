from django.shortcuts import render, redirect
from .models import AidType, Aid
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, timedelta, date


is_logged_in = True

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
    types = AidType.objects.all()
    context = {'aidtypes': types}

    # Filtro de dias
    if request.method == "GET":
        if "#oneWeek":
            seven_days_ago = datetime.today() - timedelta(days=7)
            aid = Aid.objects.filter(creation_date__gt=seven_days_ago)
            context["aid"] = aid
            return render (request, "principal/explorar.html", context)

        elif "#twoWeeks":
            fourteen_days_ago = datetime.today() - timedelta(days=14)
            aid = Aid.objects.filter(creation_date__gt=fourteen_days_ago)
            context["aid"] = aid            
            return render(request, "principal/explorar.html", context)
        
        elif "#oneMonth":
            one_month_ago = datetime.today() - timedelta(days=30)
            aid = Aid.objects.filter(creation_date__gt=one_month_ago)
            context["aid"] = aid
            return render(request, "principal/explorar.html", context)

    # Barra de Pesquisa
    if request.method == "GET":
        aid = Aid.objects.all()
        search = request.GET.get('search')
        if search:
            aid = aid.filter(title__icontains=search)
        context = {"aid": aid}


    return render(request, "principal/explorar.html", context)

# def search(request):

#     search = request.GET
#     return redirect()


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

