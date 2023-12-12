from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login   
    
def cadastro(request):
    if str(request.method) == 'GET':
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(username=nome).first()
        if user:
            messages.error(request, 'Usuarios já Registrado')
        else:
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            return redirect('login')
    
def my_login(request):
    if str(request.method) == 'GET':
        return render(request, 'login.html')
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome, password=senha)
        if user:
            login(request, user)
            return redirect('post')
        else:
            messages.error(request, 'Username ou email está incorreto')
            return render(request, 'login.html')
 