from django.shortcuts import render, redirect

# Create your views here.

# TODO: Criar os htmls para cada view

def index(request):
    return render(request, "principal/index.html")

def registro(request):
    return render(request, "principal/registro.html")

def login(request):
    return render(request, "principal/login.html")

def explorar(request):
    return render(request, "principal/explorar.html")

def visualizar(request):
    return render(request, "principal/visualizar.html")

def usuario(request):
    return render(request, "principal/usuario.html")

def editarconta(request):
    return render(request, "principal/editarconta.html")

def socorrosmeus(request):
    return render(request, "principal/socorrosmeus.html")

def criacao(request):
    return render(request, "principal/criacao.html")

def criar(request):
    return redirect('socorrosmeus')

def editar(request):
    return render(request, "principal/criacao.html") #Usa o html de criação, mas iremos carregar as informações junto

def atualizar(request):
    return redirect('socorrosmeus')

def deletar(request):
    return redirect('socorrosmeus')
