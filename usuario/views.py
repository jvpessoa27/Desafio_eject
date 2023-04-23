from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def logout(request):

    auth.logout(request)

    return redirect('login_user')

def login(request):

    if request.user.is_authenticated:
        return redirect('produtos')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        if Usuario.objects.filter(user__username=username).exists():
            username = Usuario.objects.filter(user__username=username).values_list('user__username', flat=True).get()
            user = auth.authenticate(request, username=username, password=password)
            print(username, user)
            if user is not None:
                auth.login(request, user)
                return redirect('produtos')

    return render(request, 'index.html')

def cadastro(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        username = request.POST.get('username')
        password = request.POST.get('password')
        deixe_logado = request.POST.get('deixe me logado')

        if not Usuario.objects.filter(user__username=username).exists():
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            Usuario(user=user).save()

        return redirect('login_user')

    return render(request, 'auth-register.html')

@login_required(login_url='login_user')
def perfil(request):

    usuario_perfil = Usuario.objects.get(user=request.user)

    if request.method == "POST":
        
        email = request.POST.get('email')
        usuario_perfil.user.email=email
        usuario_perfil.user.save()

    context = {
        'user': usuario_perfil,
    }

    return render(request, 'editar-usuario.html', context)

def editar(request):

    return render(request)