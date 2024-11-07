from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member_profile')
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    #feedbacks = models.ManyToManyField('Feedback', related_name='member_feedbacks',blank=True, null=True)

    def __str__(self):
        return self.nome
    
    def enviar_feedback(self, feedback_texto, tipo):
        """
        Envia um feedback sobre o produto.
        """
        feedback = Feedback.objects.create(user=self.user, feedback=feedback_texto, tipo=tipo)
        return feedback
    
    def listar_feedbacks(self):
        """
        Lista todos os feedbacks enviados pelo usuário.
        """
        return Feedback.objects.filter(user=self.user)

class Feedback(models.Model):
    TIPO_CHOICES = [
        ('Comentários gerais', 'Comentários gerais'),
        ('Sugestões de melhoria', 'Sugestões de melhoria'),
        ('Problemas tecnicos', 'Problemas tecnicos'),  # Relato de erros ou problemas técnicos.
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='feedback')
    feedback = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, default='Comentários gerais')
    data = models.DateTimeField(auto_now_add=True) #deve ser data e hr pt/br ou hr do computador

    def __str__(self):
        return f'{self.tipo} : feito por {self.member.nome} -> {self.data}'