from django.db import models
from django.contrib.auth.models import User  # Atende RF001, RF002 e RF003

# Relacionado ao CRUD de Tarefas e Cronômetro (RF004, RF005, RF006, RF010)
class Tarefa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    data_execucao = models.DateField()  # Alimenta o Calendário (RF007 e RF008)
    concluida = models.BooleanField(default=False)
    cor_etiqueta = models.CharField(max_length=7, default="#3498db")  # Personalização (RF008)
    tempo_estimado_minutos = models.IntegerField(default=0)  # Tempo associado (RF010)

    def __str__(self):
        return self.titulo

# Relacionado ao Mural Pessoal (RF009)
class PostagemMural(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postagens')
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Postagem de {self.usuario.username} em {self.data_criacao.strftime('%d/%m/%Y')}"

# Relacionado a Metas Pessoais (RF011)
class MetaPessoal(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='metas')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    prazo = models.DateField()
    atingida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

# Relacionado ao Sistema de Conquistas (RF012)
class Conquista(models.Model):
    nome = models.CharField(max_length=180)
    descricao = models.TextField()
    icone = models.CharField(max_length=50)  # Classe do ícone CSS

    def __str__(self):
        return self.nome

class ConquistaUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    conquista = models.ForeignKey(Conquista, on_delete=models.CASCADE)
    data_ganha = models.DateTimeField(auto_now_add=True)

# Relacionado ao Timer Pomodoro (RF013)
class HistoricoPomodoro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_hora_conclusao = models.DateTimeField(auto_now_add=True)
    duracao_minutos = models.IntegerField(default=60)