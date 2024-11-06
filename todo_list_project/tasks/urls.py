from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Página principal das tarefas, mostrando a lista de tarefas do usuário
    path('', views.task_list, name='task_list'),

    # Rota para o registro de novos usuários
    path('register/', views.register, name='register'),

    # Rota para adicionar uma nova tarefa
    path('add/', views.add_task, name='add_task'),

    # Rota para editar uma tarefa existente
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),

    # Rota para deletar uma tarefa existente
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),

    # Rota para alternar o estado de conclusão de uma tarefa
    path('toggle/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),

    # Inclui as URLs padrão para login, logout, etc., fornecidas pelo Django
    path('accounts/', include('django.contrib.auth.urls')),

    # Rota para login, usando a view genérica do Django
    path('login/', LoginView.as_view(), name='login'),

    # Rota para logout, redirecionando para a página de login após o logout
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]