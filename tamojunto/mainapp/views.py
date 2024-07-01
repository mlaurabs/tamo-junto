from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html") # request é a variável que representa a requisição

def cadastro(request):
    return render(request, "cadastro.html") 

def esportes(request):
    return render(request, "esportes.html") 