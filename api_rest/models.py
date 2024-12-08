from django.db import models

class User(models.Model):

    user_nickname = models.CharField(primary_key=True, max_length=100, default=" ")
    user_nome = models.CharField(max_length=180, default=" ")
    user_email = models.EmailField(default=" ")
    user_idade = models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname: {self.user_nickname} | Email: {self.user_email}'
    