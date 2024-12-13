from rest_framework import serializers
from .models import Cliente, Pet, Funcionario

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'  # Corrigido para usar "__all__"

class PetSerializer(serializers.ModelSerializer):
    pet_cliente = serializers.CharField(source='pet_cliente.cliente_nome', read_only=True)

    class Meta:
        model = Pet
        fields = '__all__'  # Corrigido para usar "__all__"

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['funcionario_nickname', 'funcionario_nome', 'funcionario_email', 'funcionario_idade']  # Este já está correto
