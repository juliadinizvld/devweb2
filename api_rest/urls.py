from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from . import views  

# Middleware para redirecionar usuários não autenticados para o login
def login_required_middleware(get_response):
    def middleware(request):
        if not request.user.is_authenticated and request.path not in ["/login/", "/cadastro/"]:
            return redirect("login")
        return get_response(request)
    return middleware

urlpatterns = [
    # Página inicial redireciona para login se o usuário não estiver autenticado
    path('', views.index, name='index'),
    
    # Autenticação
    path('login/', views.user_login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.index2, name='home'),
    
    # Admin
    path('admin/', admin.site.urls),
    
    # Rotas para Pet
    path('pets/', views.get_pets, name='get_all_pets'),
    path('pet/<str:nick>/', views.get_pet_by_nick, name='get_pet_by_nick'),
    path('pet/data/', views.pet_manager, name='pet_manager'),
    
    # Rotas para Clientes
    path('listar_clientes/', views.listar_clientes_page, name='listar_clientes_page'),
    path('clientes/', views.listar_clientes_api, name='listar_clientes_api'),
    path('editar_cliente/<str:nick>/', views.editar_cliente, name='editar_cliente'),
    path('deletar_cliente/<str:cliente_id>/', views.deletar_cliente, name='deletar_cliente'),
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    
    # Rotas para Funcionários
    path('funcionarios/', views.listar_funcionarios_api, name='listar_funcionarios_api'),
    path('editar_funcionario/<str:nick>/', views.editar_funcionario, name='editar_funcionario'),
    path('deletar_funcionario/<str:funcionario_id>/', views.deletar_funcionario, name='deletar_funcionario'),
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    
    # Rotas para Pets
    path('pets/', views.listar_pets_api, name='listar_pets_api'),
    path('editar_pet/<str:nick>/', views.editar_pet, name='editar_pet'),
    path('deletar_pet/<str:pet_id>/', views.deletar_pet, name='deletar_pet'),
    path('cadastrar_pet/', views.cadastrar_pet, name='cadastrar_pet'),
]
