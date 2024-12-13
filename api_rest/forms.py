from django import forms
from .models import Cliente, Pet, Funcionario

# Formulário de Cadastro de Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cliente_nickname', 'cliente_nome', 'cliente_email', 'cliente_idade']
        widgets = {
            'cliente_email': forms.EmailInput(attrs={'placeholder': 'Digite seu email'}),
        }

# Formulário de Cadastro de Pet
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['pet_nickname', 'pet_nome', 'pet_cliente', 'pet_idade']
        widgets = {
            'pet_cliente': forms.TextInput(attrs={'placeholder': 'Nome do Tutor'}),
        }

# Formulário de Cadastro de Funcionario
class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['funcionario_nickname', 'funcionario_nome', 'funcionario_email', 'funcionario_idade']
        widgets = {
            'funcionario_email': forms.EmailInput(attrs={'placeholder': 'Digite seu email'}),
        }
