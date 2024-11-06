from django.contrib import admin
from django.urls import path, include
from tasks import views

urlpatterns = [
    # Rota para o painel de administração do Django
    path('admin/', admin.site.urls),

    # Inclui as URLs padrão de autenticação do Django
    path('accounts/', include('django.contrib.auth.urls')),

    # URL para o registro de novos usuários
    path('register/', views.register, name='register'),

    # URL para a visualização da lista de tarefas; inclui todas as rotas do app tasks
    path('tasks/', include('tasks.urls')),  # Certifique-se de que o tasks/urls.py está configurado corretamente
]