from django.contrib import admin
from django.urls import path, include

from . import views  

urlpatterns = [

    path('', views.home, name='home'),
    
    # Rotas para Cliente
    path('clientes/', views.get_clientes, name='get_all_clientes'),  # Obter todos os clientes
    path('cliente/<str:nick>/', views.get_cliente_by_nick, name='get_cliente_by_nick'),  # Obter um cliente pelo nickname
    path('cliente/data/', views.cliente_manager, name='cliente_manager'),  # Gerenciar clientes (CRUD completo)

    # Rotas para Pet
    path('pets/', views.get_pets, name='get_all_pets'),  # Obter todos os pets
    path('pet/<str:nick>/', views.get_pet_by_nick, name='get_pet_by_nick'),  # Obter um pet pelo nickname
    path('pet/data/', views.pet_manager, name='pet_manager'),  # Gerenciar pets (CRUD completo)

    # Rotas para Funcionario
    path('funcionarios/', views.get_funcionarios, name='get_all_funcionarios'),  # Obter todos os funcionários
    path('funcionario/<str:nick>/', views.get_funcionario_by_nick, name='get_funcionario_by_nick'),  # Obter um funcionário pelo nickname
    path('funcionario/data/', views.funcionario_manager, name='funcionario_manager'),  # Gerenciar funcionários (CRUD completo)

    # Outras URLs
    path('admin/', admin.site.urls),  # URL padrão para o painel de administração do Django


    path('cadastro/cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('cadastro/pet/', views.cadastro_pet, name='cadastro_pet'),
    path('cadastro/funcionario/', views.cadastro_funcionario, name='cadastro_funcionario'),

]

 

 