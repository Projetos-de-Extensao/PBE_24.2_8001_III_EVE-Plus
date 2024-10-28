from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member_profile')
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

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
        ('Funcionalidade', 'Funcionalidade'),
        ('Desempenho', 'Desempenho'),
        ('Comentário', 'Comentário'),
        ('Sugestão', 'Sugestão'),
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='feedbacks')
    feedback = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='Comentário')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo} : feito por {self.member.nome} -> {self.data}'