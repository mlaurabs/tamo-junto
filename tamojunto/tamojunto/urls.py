"""
URL configuration for tamojunto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from mainapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastroMembro/', views.cadastroMembro, name='cadastroMembro'),
    path('cadastroInstrutor/', views.cadastroInstrutor, name='cadastroInstrutor'),
    path('esportes/', views.esportes, name="esportes"),
    path('login/', views.login, name="login"),
    path('cards/', views.cards, name="cards"),
    path('login_invalido/', views.login_invalido, name="login_invalido"),
    path('criarCard/', views.criarCard, name="criarCard"),
    path('admin/', admin.site.urls),
]
