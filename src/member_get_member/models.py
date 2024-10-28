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
    convites = models.ManyToManyField('Convite', related_name='membros_convidados', blank=True)

    def verificar_convites_aceitos(self):
        for convite in self.convites_enviados.all():
            if convite.status == 'Aceito':
                convites_aceitos = self.convites_enviados.filter(status='Aceito').count()
                # Atualiza a recompensa diretamente no banco de dados
                self.recompensas = convites_aceitos
                Member.objects.filter(pk=self.pk).update(recompensas=convites_aceitos)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
    

class Convite(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Aceito', 'Aceito'),
        ('Expirado', 'Expirado'),
    ]
    userRemetente = models.ForeignKey(Member, related_name='convites_enviados', on_delete=models.CASCADE)
    userDestinatario = models.EmailField(unique= True)
    link = models.CharField(blank=True,max_length=255, unique=True)
    # Status - quando o email for cadastrado mudara para aceito e quando passar a data de expiracao que pode ser e 1 semana mudara para expirado
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pendente')
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Convite para {self.userDestinatario} - Status: {self.status} - Token: {self.link}"

    def save(self, *args, **kwargs):
        # Verifica convites aceitos para atualizar o número de recompensas
        Member.verificar_convites_aceitos(self.userRemetente)
        # Gera link de convite se ainda não tiver sido gerado
        if not self.link:
            self.link = {str(uuid.uuid4())}
        # Salva o convite
        super().save(*args, **kwargs)

    """
    def registrar_aceitacao(self):
        if self.status == 'Pendente' and self.validar_link():
            self.status = 'Aceito'
            self.userRemetente.recompensas += 1  # Incrementa a recompensa do remetente
            self.userRemetente.save()
            self.save()
    
    def validar_link(self):
        validade = self.data_envio + timedelta(days=7)
        if timezone.now() > validade:
            self.status = 'Expirado'
            self.save()
            return False
        return True
    """
