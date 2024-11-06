from django.contrib import admin
from django.urls import path, include
from tasks import views

urlpatterns = [
    
    path('admin/', admin.site.urls),

    
    path('accounts/', include('django.contrib.auth.urls')),

   
    path('register/', views.register, name='register'),

    
    path('tasks/', include('tasks.urls')),  # Certifique-se de que o tasks/urls.py está configurado corretamente
]
