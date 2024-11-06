from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Task
from .forms import TaskForm, UserRegisterForm  # Certifique-se que o UserRegisterForm é importado corretamente
import logging

logger = logging.getLogger(__name__)

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    # Garantindo que specific_task não cause erro caso tasks esteja vazio
    specific_task = tasks[0] if tasks.exists() else None
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Associa a tarefa ao usuário autenticado
            task.save()
            messages.success(request, 'Tarefa adicionada com sucesso!')
            return redirect('task_list')  # Redireciona após a criação
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

@login_required
def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'completed': task.completed})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('task_list')
    return render(request, 'tasks/delete_task_confirm.html', {'task': task})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Conta criada com sucesso! Faça login para continuar.')
            login(request, user)
            return redirect('http://127.0.0.1:8000/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
