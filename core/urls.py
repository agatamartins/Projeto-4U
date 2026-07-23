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

    # Endpoint assíncrono para o Pomodoro e Cronômetro (Sincronização Back-end)
    path('api/pomodoro/registrar/', views.registrar_pomodoro, name='registrar_pomodoro'),
]
