from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from .forms import ClienteForm, PetForm, FuncionarioForm
from .models import Cliente, Pet, Funcionario


from .serializers import ClienteSerializer, PetSerializer, FuncionarioSerializer

import json

def home(request):
    return render(request, 'index.html')

def listar_clientes_page(request):
    clientes = Cliente.objects.all()
    return render(request, 'index.html', {'clientes': clientes})

# View para obter todos os clientes
@api_view(['GET'])
def get_clientes(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()  
        serializer = ClienteSerializer(clientes, many=True)  
        return Response(serializer.data)  
    return Response(status=status.HTTP_400_BAD_REQUEST)


# View para obter, editar ou atualizar um cliente por nickname
@api_view(['GET', 'PUT'])
def get_cliente_by_nick(request, nick):
    try:
        cliente = Cliente.objects.get(pk=nick)  # Tenta encontrar o cliente pelo nickname
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)  # Retorna os dados do cliente

    if request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data)

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)



# View para gerenciar Pets (CRUD completo)
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def pet_manager(request):
    if request.method == 'GET':
        try:
            if 'pet' in request.GET:
                pet_nickname = request.GET['pet']
                try:
                    pet = Pet.objects.get(pk=pet_nickname)
                except Pet.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = PetSerializer(pet)
                return Response(serializer.data)
            else:
                pets = Pet.objects.all()
                serializer = PetSerializer(pets, many=True)
                return Response(serializer.data)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        new_pet = request.data
        serializer = PetSerializer(data=new_pet)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        nickname = request.data['pet_nickname']
        try:
            updated_pet = Pet.objects.get(pk=nickname)
        except Pet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PetSerializer(updated_pet, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            pet_to_delete = Pet.objects.get(pk=request.data['pet_nickname'])
            pet_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Pet.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View para gerenciar Funcionários (CRUD completo)
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def funcionario_manager(request):
    if request.method == 'GET':
        try:
            if 'funcionario' in request.GET:
                funcionario_nickname = request.GET['funcionario']
                try:
                    funcionario = Funcionario.objects.get(pk=funcionario_nickname)
                except Funcionario.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = FuncionarioSerializer(funcionario)
                return Response(serializer.data)
            else:
                funcionarios = Funcionario.objects.all()
                serializer = FuncionarioSerializer(funcionarios, many=True)
                return Response(serializer.data)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        new_funcionario = request.data
        serializer = FuncionarioSerializer(data=new_funcionario)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        nickname = request.data['funcionario_nickname']
        try:
            updated_funcionario = Funcionario.objects.get(pk=nickname)
        except Funcionario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FuncionarioSerializer(updated_funcionario, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            funcionario_to_delete = Funcionario.objects.get(pk=request.data['funcionario_nickname'])
            funcionario_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Funcionario.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Funções auxiliares para obter todos os pets, clientes e funcionários
@api_view(['GET'])
def get_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.all() 
        serializer = PetSerializer(pets, many=True) 
        return Response(serializer.data) 
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_funcionarios(request):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.all()  
        serializer = FuncionarioSerializer(funcionarios, many=True) 
        return Response(serializer.data) 
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Função para obter um pet ou funcionário específico pelo nickname
@api_view(['GET'])
def get_pet_by_nick(request, nick):
    try:
        pet = Pet.objects.get(pk=nick)  # Tenta encontrar o pet pelo nickname
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PetSerializer(pet)  # Serializa os dados do pet
        return Response(serializer.data)  # Retorna os dados do pet
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_funcionario_by_nick(request, nick):
    try:
        funcionario = Funcionario.objects.get(pk=nick)  # Tenta encontrar o funcionário pelo nickname
    except Funcionario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FuncionarioSerializer(funcionario)  # Serializa os dados do funcionário
        return Response(serializer.data)  # Retorna os dados do funcionário
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Funções para cadastro de cliente, pet e funcionario
def cadastrar_cliente(request):
    if request.method == 'POST':
        # Obtendo os dados do cliente do formulário
        cliente_nome = request.POST.get('cliente_nome')
        cliente_email = request.POST.get('cliente_email')
        cliente_idade = request.POST.get('cliente_idade')
        cliente_nickname = request.POST.get('cliente_nickname')

        # Criando o novo cliente
        novo_cliente = Cliente(
            cliente_nome=cliente_nome,
            cliente_email=cliente_email,
            cliente_idade=cliente_idade,
            cliente_nickname=cliente_nickname
        )
        
        # Salvando no banco de dados
        novo_cliente.save()

        return redirect('listar_clientes_page')

    return render(request, 'clientes/cadastrar_cliente.html')

def listar_clientes_api(request):
    clientes = Cliente.objects.values('cliente_nickname', 'cliente_nome', 'cliente_email', 'cliente_idade')  
    return JsonResponse(list(clientes), safe=False)

#  editar cliente
def editar_cliente(request, nick):
    cliente = get_object_or_404(Cliente, cliente_nickname=nick)  # Alterado para buscar pelo nickname
    if request.method == 'POST':
        cliente.cliente_nome = request.POST.get('cliente_nome')
        cliente.cliente_email = request.POST.get('cliente_email')
        cliente.cliente_idade = request.POST.get('cliente_idade')
        # Salva o objeto no banco de dados
        cliente.save()
        return redirect('listar_clientes_page')

    return render(request, 'clientes/editar_clientes.html', {'cliente': cliente})

# excluir cliente
def deletar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, cliente_nickname=cliente_id)
    cliente.delete()
    return redirect('listar_clientes_page')

# Funções para cadastro de funcionario
def cadastrar_funcionario(request):
    if request.method == 'POST':
        # Obtendo os dados do cliente do formulário
        funcionario_nome = request.POST.get('funcionario_nome')
        funcionario_email = request.POST.get('funcionario_email')
        funcionario_idade = request.POST.get('funcionario_idade')
        funcionario_nickname = request.POST.get('funcionario_nickname')

        # Criando o novo funcionario
        novo_funcionario = Funcionario(
            funcionario_nome=funcionario_nome,
            funcionario_email=funcionario_email,
            funcionario_idade=funcionario_idade,
            funcionario_nickname=funcionario_nickname
        )
        
        # Salvando no banco de dados
        novo_funcionario.save()

        return redirect('listar_clientes_page')

    return render(request, 'funcionarios/cadastrar_funcionario.html')

def listar_funcionarios_api(request):
    funcionarios = Funcionario.objects.values('funcionario_nickname', 'funcionario_nome', 'funcionario_email', 'funcionario_idade')  
    return JsonResponse(list(funcionarios), safe=False)

#  editar funcionario
def editar_funcionario(request, nick):
    funcionario = get_object_or_404(Funcionario, funcionario_nickname=nick)  # Alterado para buscar pelo nickname
    if request.method == 'POST':
        funcionario.funcionario_nome = request.POST.get('funcionario_nome')
        funcionario.funcionario_email = request.POST.get('funcionario_email')
        funcionario.funcionario_idade = request.POST.get('funcionario_idade')
        # Salva o objeto no banco de dados
        funcionario.save()
        return redirect('listar_clientes_page')

    return render(request, 'funcionarios/editar_funcionario.html', {'funcionario': funcionario})

#  excluir cliente
def deletar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, funcionario_nickname=funcionario_id)
    funcionario.delete()
    return redirect('listar_clientes_page')


def cadastrar_pet(request):
    if request.method == 'POST':
        pet_nickname = request.POST.get('pet_nickname')
        pet_nome = request.POST.get('pet_nome')
        pet_idade = request.POST.get('pet_idade')
        pet_cliente_nickname = request.POST.get('pet_cliente')  # Obtém o nickname do cliente selecionado

        # Busca o cliente associado
        pet_cliente = Cliente.objects.get(cliente_nickname=pet_cliente_nickname)

        # Cria o pet
        novo_pet = Pet(
            pet_nickname=pet_nickname,
            pet_nome=pet_nome,
            pet_idade=pet_idade,
            pet_cliente=pet_cliente
        )
        novo_pet.save()

       
        return redirect('listar_clientes_page')

    # Passa a lista de clientes para o template
    clientes = Cliente.objects.all()
    return render(request, 'pets/cadastrar_pet.html', {'clientes': clientes})


def listar_pets_api(request):
    pets = Pet.objects.values('pet_nickname', 'pet_nome', 'pet_idade', 'pet_cliente__cliente_nome')  # Inclui o nome do cliente relacionado
    return JsonResponse(list(pets), safe=False)


#  editar  pet
def editar_pet(request, nick):
    pet = get_object_or_404(Pet, pet_nickname=nick)

      # Obtém todos os clientes
    clientes = Cliente.objects.all()  
    if request.method == 'POST':
        pet.pet_nome = request.POST.get('pet_nome')
        pet.pet_idade = request.POST.get('pet_idade')
        pet.pet_cliente_id = request.POST.get('pet_cliente') 
        pet.save()
        return redirect('listar_clientes_page')

    return render(request, 'pets/editar_pet.html', {'pet': pet, 'clientes': clientes})



def deletar_pet(request, pet_id):
    pet = get_object_or_404(Pet, pet_nickname=pet_id)  
    pet.delete()
    return redirect('listar_clientes_page')

