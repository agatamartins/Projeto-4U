from django import forms
from django.contrib.auth.models import User
from .models import Tarefa, PostagemMural, MetaPessoal

# Formulário de Cadastro de Usuário (RF001)
class UsuarioCadastroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Senha')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

# Formulário para criar tarefas (RF004)
class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'data_execucao', 'cor_etiqueta', 'tempo_estimado_minutos']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'data_execucao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cor_etiqueta': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'tempo_estimado_minutos': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Formulário para postagens do Mural (RF009)
class PostagemMuralForm(forms.ModelForm):
    class Meta:
        model = PostagemMural
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Escreva uma anotação ou lembrete...'}),
        }

# Formulário para criar metas pessoais (RF011)
class MetaPessoalForm(forms.ModelForm):
    class Meta:
        model = MetaPessoal
        fields = ['titulo', 'descricao', 'prazo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'prazo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

# Formulário de edição de perfil (RF003)
class PerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }