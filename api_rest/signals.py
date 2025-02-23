from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Cliente, Funcionario

@receiver(post_save, sender=Cliente)
@receiver(post_save, sender=Funcionario)
def enviar_email_boas_vindas(sender, instance, created, **kwargs):
    if created:
        if isinstance(instance, Cliente):
            # Para Cliente
            mensagem = f"Olá {instance. cliente_nickname},\n\nBem-vindo à nossa creche de pets! Estamos felizes em tê-lo conosco."
            send_mail(
                'Boas-vindas à nossa Creche de Pets!',
                mensagem,
                settings.DEFAULT_FROM_EMAIL,
                [instance.cliente_email],
                fail_silently=False,
            )
        elif isinstance(instance, Funcionario):
            # Para Funcionario
            mensagem = f"Olá {instance.funcionario_nickname},\n\nBem-vindo à nossa equipe! Estamos felizes em tê-lo conosco."
            send_mail(
                'Boas-vindas à nossa Creche de Pets!',
                mensagem,
                settings.DEFAULT_FROM_EMAIL,
                [instance.funcionario_email],
                fail_silently=False,
            )