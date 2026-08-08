from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('calendario/', views.calendario_view, name='calendario'),
    path('conquistas/', views.conquistas_view, name='conquistas'),

    # Perfil do usuário (RF003)
    path('perfil/', views.perfil_view, name='perfil'),

    # CRUD de Tarefas (RF004, RF005, RF006) e conclusão/personalização (RF008)
    path('tarefas/nova/', views.criar_tarefa_view, name='criar_tarefa'),
    path('tarefas/<int:pk>/editar/', views.editar_tarefa_view, name='editar_tarefa'),
    path('tarefas/<int:pk>/excluir/', views.excluir_tarefa_view, name='excluir_tarefa'),
    path('tarefas/<int:pk>/concluir/', views.concluir_tarefa_view, name='concluir_tarefa'),

    # Metas pessoais (RF011)
    path('metas/<int:pk>/concluir/', views.concluir_meta_view, name='concluir_meta'),

    # Endpoint assíncrono para o Pomodoro e Cronômetro (Sincronização Back-end) (RF013)
    path('api/pomodoro/registrar/', views.registrar_pomodoro, name='registrar_pomodoro'),
]
