from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Importando os modelos
from .models import Cliente, Pet, Funcionario

# Importando os serializers
from .serializers import ClienteSerializer, PetSerializer, FuncionarioSerializer

import json


# View para obter todos os clientes
@api_view(['GET'])
def get_clientes(request):

    if request.method == 'GET':
        clientes = Cliente.objects.all()  # Pega todos os objetos da tabela Cliente
        serializer = ClienteSerializer(clientes, many=True)  # Serializa a lista de clientes
        return Response(serializer.data)  # Retorna os dados serializados

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
            serializer.save()  # Atualiza o cliente com os dados fornecidos
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


# View para gerenciar clientes (CRUD completo)
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def cliente_manager(request):

    # GET - Listar ou pegar cliente por nickname
    if request.method == 'GET':
        try:
            if 'cliente' in request.GET:
                cliente_nickname = request.GET['cliente']
                try:
                    cliente = Cliente.objects.get(pk=cliente_nickname)
                except Cliente.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = ClienteSerializer(cliente)
                return Response(serializer.data)
            else:
                clientes = Cliente.objects.all()
                serializer = ClienteSerializer(clientes, many=True)
                return Response(serializer.data)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # POST - Criar um novo cliente
    if request.method == 'POST':
        new_cliente = request.data
        serializer = ClienteSerializer(data=new_cliente)

        if serializer.is_valid():
            serializer.save()  # Cria um novo cliente
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    # PUT - Atualizar cliente
    if request.method == 'PUT':
        nickname = request.data['cliente_nickname']
        try:
            updated_cliente = Cliente.objects.get(pk=nickname)
        except Cliente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ClienteSerializer(updated_cliente, data=request.data)

        if serializer.is_valid():
            serializer.save()  # Atualiza o cliente com os dados fornecidos
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    # DELETE - Deletar cliente
    if request.method == 'DELETE':
        try:
            cliente_to_delete = Cliente.objects.get(pk=request.data['cliente_nickname'])
            cliente_to_delete.delete()  # Deleta o cliente
            return Response(status=status.HTTP_202_ACCEPTED)
        except Cliente.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Similar para Pet
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


# Similar para Funcionario
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
        
# Função para obter todos os pets
@api_view(['GET'])
def get_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.all()  # Pega todos os objetos da tabela Pet
        serializer = PetSerializer(pets, many=True)  # Serializa a lista de pets
        return Response(serializer.data)  # Retorna os dados serializados

    return Response(status=status.HTTP_400_BAD_REQUEST)


# Função para obter um pet específico pelo nickname
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


# Função para obter todos os funcionários
@api_view(['GET'])
def get_funcionarios(request):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.all()  # Pega todos os objetos da tabela Funcionario
        serializer = FuncionarioSerializer(funcionarios, many=True)  # Serializa a lista de funcionários
        return Response(serializer.data)  # Retorna os dados serializados

    return Response(status=status.HTTP_400_BAD_REQUEST)


# Função para obter um funcionário específico pelo nickname
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

    
    