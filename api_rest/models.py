from django.db import models
from django.contrib.auth.models import AbstractUser

class Cliente(models.Model):
    cliente_nickname = models.CharField(primary_key=True, max_length=100, default=" ")
    cliente_nome = models.CharField(max_length=180, default=" ")
    cliente_email = models.EmailField(default=" ")
    cliente_idade = models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname: {self.cliente_nickname} | Email: {self.cliente_email}'

    class Meta:
        verbose_name_plural = "Clientes"
        ordering = ['cliente_nome']
        
class Pet(models.Model):
    pet_nickname = models.CharField(primary_key=True, max_length=100, default=" ")
    pet_nome = models.CharField(max_length=180, default=" ")
    pet_cliente = models.ForeignKey(
        Cliente,  # Relação com o modelo Cliente
        on_delete=models.CASCADE,  # Se o cliente for deletado, os pets associados também serão deletados
        related_name='pets',  # Nome utilizado para acessar os pets de um cliente
    )
    pet_idade = models.IntegerField(default=0)

    def __str__(self):
        return f'Pet: {self.pet_nickname} | Nome: {self.pet_nome} | Tutor: {self.pet_cliente.cliente_nome}'

    class Meta:
        verbose_name_plural = "Pets"
        ordering = ['pet_nome']


class Funcionario(models.Model):
    funcionario_nickname = models.CharField(primary_key=True, max_length=100, default=" ")
    funcionario_nome = models.CharField(max_length=180, default=" ")
    funcionario_email = models.EmailField(default=" ")
    funcionario_idade = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Funcionario: {self.funcionario_nickname} | Email: {self.funcionario_email}'
    
    class Meta:
        verbose_name_plural = "Funcionarios"
        ordering = ['funcionario_nome']


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Aqui você pode adicionar outros campos, se necessário
