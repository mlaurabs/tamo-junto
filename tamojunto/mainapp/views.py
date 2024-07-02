from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html") # request é a variável que representa a requisição

def cadastro(request):
    return render(request, "cadastro.html") 

def cadastroMembro(request):
    return render(request, "cadastroMembro.html")

def cadastroInstrutor(request):
    return render(request, "cadastroInstrutor.html") 

def esportes(request):
    return render(request, "esportes.html") 

def login(request):
    return render(request, "login.html") 

def cards(request):
    return render(request, "cards.html") 