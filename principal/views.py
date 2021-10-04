from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .form import AidForm, AidPhotosForm, RegistrationForm, EditProfileForm
from .models import AidType, Aid, AidPhotos, User, UserManager
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime, timedelta, date
from django.contrib import messages # Vai importar as mensagens do django
from django.conf import settings


def home(request):
    return render(request, "principal/home.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cadastro concluido com sucesso!')
            print('Registrado')

            # Loga o usuário após se cadastrar.
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'Formulário inválido!')

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
                return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'Email ou Senha incorretos!')
            return redirect('login')
    return render(request, "principal/login.html")

def log_out(request):
    logout(request)
    return redirect('home')

def explore(request):
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


def seeAid(request, id):
    return render(request, "principal/socorro.html")

@login_required(login_url="/login/")
def user(request, id):
    userViewed = User.objects.get(pk=id)
    return render(request, "principal/account.html", {'userViewed':userViewed})

@login_required(login_url="/login/")
def edit_account(request, id):
    userData = User.objects.get(pk=id)
    userForm = EditProfileForm(instance = userData)
    user = User.objects.get(pk=id)
    if request.user.id == getattr(user, 'id'):
        if request.method == 'POST':
            print('\n\nFoi POST\n\n')
            userUpdate = EditProfileForm(request.POST, request.FILES, instance= userData)
            if userUpdate.is_valid():
                userUpdate.save()
                return redirect(f'/user/{id}/')
            else:
                print("\n\nForm é invalido")
                print('CPF: ', userUpdate['cpf'].value(), " X ", userData.cpf)
                print("\n\n")
        else:
            print('\n\nNão foi POST\n\n')
            return render(request, "principal/editAccount.html", {'userForm': userForm, 'userData':userData})  
    else:
        return redirect(f'/user/{id}/')

@login_required(login_url="/login/")
def socorros_meus(request):
    return render(request, "principal/socorrosmeus.html")

@login_required(login_url="/login/")
def needAid(request):
    context = {}
    context['form'] = AidForm(author=request.user)
    context['image_form'] = AidPhotosForm()
    return render(request, "principal/needAid.html", context)

@login_required(login_url="/login/")
def createAid(request):

    # A criação de socorros consiste em 2 forms, o primeiro para o socorro em sí (título, descrição e autor) e o segundo 
    # para as imagens (socorro, imagem e descrição) e para seu input de imagens que possui "multiple" (mais de uma imagem), é necessário que a lista seja 
    # recuperada pelo request.FILES.getlist separadamente. 
    # Os 2 forms devem ser validos para que o processo de salvamento ocorra, o form de socorro retorna uma instancia que será armazenada e será o socorro da
    # instancia do form de imagens (o campo "aid" do model AidPhotos) 

    form = AidForm(request.POST, author=request.user) # Form do Socorro em sí
    
    img_form = AidPhotosForm(request.POST, request.FILES) # Contém os dados do form de imagens (seu ImageField pode conter apenas 1 imagem)
    images = request.FILES.getlist('image') # Contém a lista de imagens pegas pelo request

    print('\n\n\n\nRequest: ', request.FILES.getlist('image'), '\n\n\n\n') 

    if form.is_valid() and img_form.is_valid():
        print('\n\n\n\nEntrou\n\n\n\n') 
        form = form.save()
        description = img_form.cleaned_data['description']
        for img in images:
            print(img)
            AidPhotos.objects.create(aid=form, image=img, description=description)
        print("\n\n\n\n")
        return redirect('home')

    print('\n\n\n\nErrors: ', img_form.errors, '\n\n\n\n') 


@login_required(login_url="/login/")
def deletar(request, pk):
    aid_post = Aid.objects.get(pk=pk)
    print('\n\n\n\n', getattr(aid_post, 'author').id, ' x ', request.user.id, '\n\n\n\n')

    if request.user.id == getattr(aid_post, 'author').id:
        aid_post.delete()
        print('\n\n\n\nSocorro deletado com sucesso\n\n\n\n')
    else:
        print('\n\n\n\nEsse socorro não é seu\n\n\n\n')

    return redirect('home')

def delete(request, pk): #Deletar Usuário
    user = User.objects.get(pk=pk)
    if request.user.id == getattr(user, 'id'):
        user.delete()
    return redirect('home')