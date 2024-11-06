# Sistema de Tarefas
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.x-green.svg)](https://www.djangoproject.com/)

Um aplicativo web de gerenciamento de tarefas construído com Django, permitindo aos usuários criar, editar, excluir e acompanhar suas tarefas diárias.

## Índice
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Como Utilizar](#como-utilizar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Funcionalidades

- Autenticação de usuários (login/logout)
- Criação de novas tarefas
- Visualização de lista de tarefas
- Edição de tarefas existentes
- Marcação de tarefas como concluídas
- Exclusão de tarefas

## Requisitos

- Python 3.12.3
- Django 5.1.3
- Ambiente virtual (venv)

## Instalação

1. Clone o repositório:

2. Crie e ative um ambiente virtual:

python -m venv venv source venv/bin/activate # No Windows use venv\Scripts\activate


3. Instale as dependências:

pip install -r requirements.txt


4. Configure o banco de dados:

python manage.py migrate


5. Crie um superusuário (opcional):

python manage.py createsuperuser


6. Inicie o servidor de desenvolvimento:

python manage.py runserver


## Como Utilizar

1. Acesse a página de login: http://127.0.0.1:8000/accounts/login/
- Se não tiver uma conta, clique em "Não tem uma conta?" para criar uma.

2. Após o login, você será redirecionado para a página de lista de tarefas.

3. Na página de tarefas, você pode:
- Criar uma nova tarefa
- Marcar tarefas como concluídas
- Editar tarefas existentes
- Excluir tarefas
- Fazer logout para entrar em uma nova conta

## Estrutura do Projeto

### URLs Principais

- `/accounts/login/` - Página de login do usuário
- `/tasks/` - Página principal que exibe todas as tarefas
- `/tasks/new/` - Página para criar uma nova tarefa
- `/tasks/<id>/edit/` - Página para editar uma tarefa específica
- `/tasks/<id>/delete/` - Rota para excluir uma tarefa específica

### Views

- `LoginView` e `LogoutView`: Controlam o login e logout dos usuários
- `TaskListView`: Exibe todas as tarefas do usuário
- `TaskCreateView`: Permite que o usuário crie uma nova tarefa
- `TaskUpdateView`: Permite que o usuário edite uma tarefa existente
- `TaskDeleteView`: Permite que o usuário exclua uma tarefa

### Templates HTML

Os templates estão localizados nas pastas `templates/tasks` e `templates/registration`, incluindo arquivos para cada página da aplicação.

### Modelos (Models)

O modelo principal é `Task`, que representa uma tarefa e inclui campos como título, descrição, data de criação e status de conclusão.

### Configurações

Certifique-se de adicionar 'Tasks' em `INSTALLED_APPS` no arquivo `settings.py`.

Desenvolvido por [Gustavo Rossi](https://github.com/GustavoRossii)
