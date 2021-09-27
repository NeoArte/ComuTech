from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .form import AidForm, RegistrationForm
from .models import AidType, Aid
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, timedelta, date


is_logged_in = True

# As funções com testes "if_logged_in" verificam se o usuário está logado, se estiver acessa a página normalmente e 
# caso contrário é redirecionado para a página de login (determinadno que é necessário estar logado), as páginas com apenas redirects são as que fazem
# ações HTTP (ex: POST) e devolvem o úsuario para alguma tela, geralmente a anterior.

def index(request):
    return render(request, "principal/index.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('Registrado')

            # Loga o usuário após se cadastrar.
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('explorar')
            return redirect('index')

    form = RegistrationForm() 
    context = {
        'form': form,
    }
    return render(request, "principal/register.html", context)


def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # next se refere a página para qual o usuario será redirecionado, 
            # ela é adicionado ao URL de onde passamos para um input hidden e retornamos aqui
            next = request.POST.get('next') 
            if next is not None:
                print("\n\nLOGADO\n\n")
                login(request, user)
                #Aid.objects.filter(type__exact=f"{type}")
                return redirect(next)
            elif next is None:
                login(request, user)
                return redirect('index')
        else:
            return redirect('login')

    return render(request, "principal/login.html")

def log_out(request):
    logout(request)
    return redirect('index')

def explorar(request, extra_context=None):
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

        # Scroll Infinito 

    context = {
        'entry_list': AidType.objects.all(),
    }
    if extra_context is not None:
        context.update(extra_context)
    
    return render(request, "principal/explorar.html", context)

# def search(request):

#     search = request.GET
#     return redirect()


def visualizar(request):
    return render(request, "principal/socorro.html")

@login_required(login_url="/login/")
def usuario(request):
    return render(request, "principal/usuario.html")

@login_required(login_url="/login/")
def editarconta(request):
    return render(request, "principal/editarconta.html")

@login_required(login_url="/login/")
def socorros_meus(request):
    return render(request, "principal/socorrosmeus.html")

@login_required(login_url="/login/")
def criacao(request):
    context = {}
    context['form'] = AidForm(author=request.user)
    return render(request, "principal/criacao-customuser.html", context)

@login_required(login_url="/login/")
def criar(request):
    form = AidForm(request.POST, author=request.user)
    if form.is_valid():
        form.save()
        return redirect('socorrosmeus')


@login_required(login_url="/login/")
def deletar(request, pk):
    aid_post = Aid.objects.get(pk=pk)
    print('\n\n\n\n', getattr(aid_post, 'author').id, ' x ', request.user.id, '\n\n\n\n')

    if request.user.id == getattr(aid_post, 'author').id:
        aid_post.delete()
        print('\n\n\n\nSocorro deletado com sucesso\n\n\n\n')
    else:
        print('\n\n\n\nEsse socorro não é seu\n\n\n\n')

    return redirect('index')

