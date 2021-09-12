from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "principal/index.html")

def registro(request):
    return render(request, "principal/index.html")

def login(request):
    return render(request, "principal/index.html")

def explorar(request):
    return render(request, "principal/index.html")

def visualizar(request):
    return render(request, "principal/index.html")

def usuario(request):
    return render(request, "principal/index.html")

def editarconta(request):
    return render(request, "principal/index.html")

def socorrosmeus(request):
    return render(request, "principal/index.html")

def criacao(request):
    return render(request, "principal/index.html")

def criar(request):
    return redirect('socorrosmeus')

def editar(request):
    return render(request, "principal/index.html") #Usa o html de criação, mas iremos carregar as informações junto

def atualizar(request):
    return redirect('socorrosmeus')

def deletar(request):
    return redirect('socorrosmeus')
