from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    
    path('', views.task_list, name='task_list'),

    
    path('register/', views.register, name='register'),

    
    path('add/', views.add_task, name='add_task'),

    
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),

    
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),

    
    path('toggle/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),

   
    path('accounts/', include('django.contrib.auth.urls')),

    
    path('login/', LoginView.as_view(), name='login'),

    
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
