from rest_framework import serializers
from .models import Cliente, Pet, Funcionario

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '_all_'

class PetSerializer(serializers.ModelSerializer):
    pet_cliente = serializers.CharField(source='pet_cliente', read_only=True)

    class Meta:
        model = Pet
        fields = ['pet_nickname', 'pet_cliente', 'cliente_idade']

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['funcionario_nickname', 'funcionario_nome', 'funcionario_email', 'funcionario_idade']