from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import timedelta
from django.utils import timezone


class Usuario(models.Model):
    """
    Extensão do modelo de usuário padrão do Django, caso precise de informações adicionais.
    """

    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Convite(models.Model):
    """
    Modelo que representa os convites enviados por um usuário.
    """

    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Aceito', 'Aceito'),
        ('Expirado', 'Expirado'),
    ]
    
    link = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pendente')
    data_envio = models.DateTimeField(auto_now_add=True)
    usuario_remetente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='convites_enviados')
    usuario_convidado = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='convite_aceito')

    def gerar_link(self):
        """
        Gera um link único para o convite usando UUID.
        """

        self.link = str(uuid.uuid4())
        self.save()
        return f"http://iquirium.com/cadastro/{self.link}"

    def validar_link(self):
        """
        Verifica se o convite ainda é válido (não expirado ou já aceito).
        """

        validade = self.data_envio + timedelta(days=7)  # Exemplo de validade de 7 dias
        if self.status == 'Aceito' or self.data_envio + timedelta(days=7) < timezone.now():
            return False
        return True

    def registrar_aceitacao(self, usuario_convidado):
        """
        Atualiza o status do convite para 'Aceito' e vincula o novo usuário.
        """
        
        if self.validar_link():
            self.status = 'Aceito'
            self.usuario_convidado = usuario_convidado
            self.save()
        else:
            raise Exception('Convite inválido ou expirado')

    def __str__(self):
        return f"Convite de {self.usuario_remetente.nome} - Status: {self.status}"


class Recompensa(models.Model):
    """
    Modelo que representa as recompensas recebidas por usuários.
    """
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='recompensas')
    descricao = models.CharField(max_length=255, default='Recompensa por convite')
    data_concedida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recompensa para {self.usuario.nome} - {self.descricao}"


def conceder_recompensa(usuario):
    """
    Lógica para conceder uma recompensa ao usuário que enviou o convite.
    """
    Recompensa.objects.create(usuario=usuario, descricao="Recompensa por ter convidado um novo usuário")
