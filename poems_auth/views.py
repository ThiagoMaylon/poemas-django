from django.shortcuts import render
from .forms import LoginModelFoms, CadastroModelForms

def login(request):
    
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')