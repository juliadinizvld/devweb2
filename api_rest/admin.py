from django.contrib import admin

from .models import Cliente, Pet, Funcionario 

admin.site.register(Cliente)
admin.site.register(Pet)
admin.site.register(Funcionario)