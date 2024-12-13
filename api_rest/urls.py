from django.contrib import admin
from django.urls import path, include

from . import views  

urlpatterns = [

    path('', views.home, name='home'),
    
  

    # Rotas para Pet
    path('pets/', views.get_pets, name='get_all_pets'),  # Obter todos os pets
    path('pet/<str:nick>/', views.get_pet_by_nick, name='get_pet_by_nick'),  # Obter um pet pelo nickname
    path('pet/data/', views.pet_manager, name='pet_manager'),  # Gerenciar pets (CRUD completo)

  

    # Outras URLs
    path('admin/', admin.site.urls),  





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