from django.shortcuts import render
from .forms import PostModelFrom
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'index.html', context)

@login_required(login_url='/auth/login')
def post(request):
    if str(request.method) == 'POST':
        form = PostModelFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Postagem criada com sucesso')
            form = PostModelFrom()
        else:
            messages.error(request, 'Houver um Erro')
    else:
        form = PostModelFrom()
            
    context = {
        'form': form
    }
    return render(request, 'post.html', context)