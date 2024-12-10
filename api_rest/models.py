from django.db import models

class Cliente(models.Model):

    cliente_nickname = models.CharField(primary_key=True, max_length=100, default=" ")
    cliente_nome = models.CharField(max_length=180, default=" ")
    cliente_email = models.EmailField(default=" ")
    cliente_idade = models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname: {self.cliente_nickname} | Email: {self.cliente_email}'
    
class Pet(models.Model):

    pet_nickname = models.CharField(primary_key=True, max_length=100, default=" ")
    pet_cliente = models.CharField(max_length=180, default=" ")
    cliente_idade = models.IntegerField(default=0)

    def __str__(self):
        return f'Pet: {self.pet_nickname} | Tutor: {self.pet_cliente}'

class Funcionario(models.Model):

    funcionario_nickname = models.CharField(primary_key=True, max_length=100, default=" ")
    funcionario_nome = models.CharField(max_length=180, default=" ")
    funcionario_email = models.EmailField(default=" ")
    funcionario_idade = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Funcionario: {self.funcionario_nickname} | Email: {self.funcionario_email}'