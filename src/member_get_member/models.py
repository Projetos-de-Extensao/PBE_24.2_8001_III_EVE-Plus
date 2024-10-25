from typing import Any
from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime, timedelta



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
    #UserRemetente - ja eh preenchido automaticamente identificandoo o user que ja esta logado
     #usuario logado faz o envio do convite, como obter o id de identiicacao do usuario
    userRemetente = models.ForeignKey(Member, related_name='convites', on_delete=models.CASCADE)
    userDestinatario = models.EmailField(unique= True)
    link = models.CharField(max_length=255, unique=True)
    #   Status - nao aparece no django adimin e eh criado automaticamente como pendente, porem quando o email for cadastrado mudara para aceito e 
    # quando passar a data de expiracao que pode ser e 1 semana mudara para expirado
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pendente')
    data_envio = models.DateTimeField(auto_now_add=True)

    def criar_convite(self):
        pass

    def gerarLink(self):
        self.link = str(uuid.uuid4())
        #self.data_expiracao = datetime.now() + timedelta(days=7)
        self.save()
        return f"http://iquirium.com/cadastro/{self.link}"

    def __str__(self):
        return self.userDestinatario +" - "+self.link

"""
    def save(self, *args, **kwargs):
        if not self.link:
            self.gerarLink()
        super().save(*args, **kwargs)

class Sistema(models.Model):
    def conceder_recompensa(self, member, convite):
        if convite.status == 'Aceito':
            member.recompensas += 1
            member.save()
        else:
            pass

    def registrar_aceitacao(self, convite):
        if convite.status == 'Pendente':
            convite.status = 'Aceito'
            convite.save()
        else:
            pass

    def validar_link(self, convite):
        if convite.data_expiracao < datetime.now():
            convite.status = 'Expirado'
            convite.save()
        else:
            pass
"""
