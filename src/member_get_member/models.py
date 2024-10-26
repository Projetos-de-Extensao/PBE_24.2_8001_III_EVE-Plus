from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver



class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    recompensas = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
    

class Convite(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Aceito', 'Aceito'),
        ('Expirado', 'Expirado'),
    ]
    userRemetente = models.ForeignKey(Member, related_name='convites', on_delete=models.CASCADE)
    userDestinatario = models.EmailField(unique= True)
    link = models.CharField(blank=True,max_length=255, unique=True)
    #   Status - quando o email for cadastrado mudara para aceito e 
    # quando passar a data de expiracao que pode ser e 1 semana mudara para expirado
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pendente')
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Convite para {self.userDestinatario} - Status: {self.status}"

    def save(self, *args, **kwargs):
        # Gera um link automaticamente ao salvar, se ainda não tiver sido gerado
        if self.link:
            self.link = f"http://iquirium.com/cadastro/{self.link}"
        if not self.link:
            self.link = f"http://iquirium.com/cadastro/{str(uuid.uuid4())}"
        super().save(*args, **kwargs)

    def registrar_aceitacao(self):
        """
        Marca o convite como 'Aceito' e concede recompensa ao remetente.
        """
        if self.status == 'Pendente' and self.validar_link():
            self.status = 'Aceito'
            self.save()
            # Conceder recompensa ao remetente
            self.userRemetente.recompensas += 1
            self.userRemetente.save()

    def validar_link(self):
        """
        Verifica se o convite ainda está válido (dentro do prazo de 7 dias).
        """
        validade = self.data_envio + timedelta(days=7)
        if timezone.now() > validade:
            self.status = 'Expirado'
            self.save()
            return False
        return True


"""

class Sistema(models.Model):

    def conceder_recompensa(self, member, convite):
        if convite.status == 'Aceito':
            member.recompensas += 1
            member.save()
        else:
            pass

"""
