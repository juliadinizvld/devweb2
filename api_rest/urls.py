from django.contrib import admin
from django.urls import path, include

from . import views  

urlpatterns = [

    path('', views.home, name='home'),
    
    # Rotas para Cliente
   # path('clientes/', views.get_clientes, name='get_all_clientes'),  # Obter todos os clientes
    #path('cliente/<str:nick>/', views.get_cliente_by_nick, name='get_cliente_by_nick'),  # Obter um cliente pelo nickname
    #path('cliente/data/', views.cliente_manager, name='cliente_manager'),  # Gerenciar clientes (CRUD completo)

    # Rotas para Pet
    path('pets/', views.get_pets, name='get_all_pets'),  # Obter todos os pets
    path('pet/<str:nick>/', views.get_pet_by_nick, name='get_pet_by_nick'),  # Obter um pet pelo nickname
    path('pet/data/', views.pet_manager, name='pet_manager'),  # Gerenciar pets (CRUD completo)

    # # Rotas para Funcionario
    # path('funcionarios/', views.get_funcionarios, name='get_all_funcionarios'),  # Obter todos os funcionários
    # path('funcionario/<str:nick>/', views.get_funcionario_by_nick, name='get_funcionario_by_nick'),  # Obter um funcionário pelo nickname
    # path('funcionario/data/', views.funcionario_manager, name='funcionario_manager'),  # Gerenciar funcionários (CRUD completo)

    # Outras URLs
    path('admin/', admin.site.urls),  # URL padrão para o painel de administração do Django


    #path('cadastro/cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    # path('cadastro/pet/', views.cadastro_pet, name='cadastro_pet'),
    # path('cadastro/funcionario/', views.cadastro_funcionario, name='cadastro_funcionario'),



    path('listar_clientes/', views.listar_clientes_page, name='listar_clientes_page'),
    path('clientes/', views.listar_clientes_api, name='listar_clientes_api'),
    path('editar_cliente/<str:nick>/', views.editar_cliente, name='editar_cliente'),
    path('deletar_cliente/<str:cliente_id>/', views.deletar_cliente, name='deletar_cliente'),
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),  # Implementar a view para cadastrar

 
    path('funcionarios/', views.listar_funcionarios_api, name='listar_funcionarios_api'),
    path('editar_funcionario/<str:nick>/', views.editar_funcionario, name='editar_funcionario'),
    path('deletar_funcionario/<str:funcionario_id>/', views.deletar_funcionario, name='deletar_funcionario'),
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),  # Implementar a view para cadastrar

 path('pets/', views.listar_pets_api, name='listar_pets_api'),
    path('editar_pet/<str:nick>/', views.editar_pet, name='editar_pet'),
    path('deletar_pet/<str:pet_id>/', views.deletar_pet, name='deletar_pet'),
    path('cadastrar_pet/', views.cadastrar_pet, name='cadastrar_pet'),  # Implementar a view para cadastrar

]