from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as login_django
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html") # request é a variável que representa a requisição

def cadastro(request):
    return render(request, "cadastro.html") 

def cadastroMembro(request):
    if(request.method == "GET"):
        return render(request, "cadastroMembro.html")
    else:
        username = request.POST["username"]
        email = request.POST["email"]
        senha = request.POST["password"]

        user = User.objects.filter(username=username).first()
        if(user):
            return HttpResponse('Já exsite usuário com esse username')
    
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
    
        return redirect("login")


def cadastroInstrutor(request):
    if(request.method == "GET"):
        return render(request, "cadastroInstrutor.html")
    else:
        username = request.POST["username"]
        email = request.POST["email"]
        senha = request.POST["password"]

        user = User.objects.filter(username=username).first()
        if(user):
            return HttpResponse('Já exsite usuário com esse username')
    
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
    
        return redirect("login") 

def esportes(request):
    return render(request, "esportes.html") 

def login(request):
    if(request.method == "GET"):
        return render(request, "login.html") 
    else:
        username = request.POST.get("username")
        senha = request.POST.get("password")  # Certifique-se de usar "password"

        user = authenticate(username=username, password=senha)
        if(user): #usuario existente
            login_django(request, user)
            return redirect("home")
        else:
            return redirect("login_invalido")

def cards(request):
    if(request.user.is_authenticated):
        return render(request, "cards.html") 
    else:
        return redirect("login")


def login_invalido(request):
    return render(request, "login_invalido.html") 

def criarCard(request):
    if(request.user.is_authenticated):
        return render(request, "criarCard.html") 
    else:
        return redirect("login")

