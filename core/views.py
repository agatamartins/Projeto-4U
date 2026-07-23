from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tarefa, PostagemMural, MetaPessoal, ConquistaUsuario, HistoricoPomodoro
import json

def landing_page(request):
    return render(request, 'core/landing.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'core/login.html')
    return render(request, 'core/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'core/cadastro.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
            return render(request, 'core/cadastro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
            return render(request, 'core/cadastro.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user = authenticate(request, username=username, password=password)
        login(request, user)
        messages.success(request, 'Conta criada com sucesso!')
        return redirect('dashboard')

    return render(request, 'core/cadastro.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('landing_page')

@login_required
def dashboard_view(request):
    tarefas = Tarefa.objects.filter(usuario=request.user, concluida=False)
    postagens = PostagemMural.objects.filter(usuario=request.user).order_by('-data_criacao')

    context = {
        'tarefas': tarefas,
        'postagens': postagens,
    }
    return render(request, 'core/dashboard.html', context)

@login_required
def calendario_view(request):
    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'core/calendario.html', {'tarefas': tarefas})

@login_required
def conquistas_view(request):
    metas = MetaPessoal.objects.filter(usuario=request.user)
    conquistas = ConquistaUsuario.objects.filter(usuario=request.user)
    return render(request, 'core/conquistas.html', {'metas': metas, 'conquistas': conquistas})

@login_required
def registrar_pomodoro(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        duracao = data.get('duracao', 25)

        HistoricoPomodoro.objects.create(
            usuario=request.user,
            duracao_minutos=duracao
        )
        return JsonResponse({'status': 'sucesso', 'mensagem': 'Ciclo Pomodoro registrado com sucesso!'})
    return JsonResponse({'status': 'erro'}, status=400)
