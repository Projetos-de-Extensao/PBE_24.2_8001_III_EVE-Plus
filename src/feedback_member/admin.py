from django.contrib import admin
from .models import Feedback, Member

# Inline para exibir feedbacks na página de detalhes de um Member
class FeedbackInline(admin.TabularInline):
    model = Feedback
    fields = ['feedback', 'data', 'tipo']
    readonly_fields = ['data']  # Campos de leitura
    extra = 0  # Evita criação automática de novos feedbacks

class MemberAdmin(admin.ModelAdmin):
    exclude = ('nome', 'user', 'email')  # Oculta os campos
    inlines = [FeedbackInline]  # Adiciona feedbacks na página de detalhes de um Member

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        obj.nome = obj.nome or obj.user.username
        obj.email = obj.email or obj.user.email
        obj.save()

class FeedbackAdmin(admin.ModelAdmin):
    exclude = ('member',)  # Oculta o campo member no FeedbackAdmin

    def save_model(self, request, obj, form, change):
        if hasattr(request.user, 'member'):
            obj.member = request.user.member  # Define o member como o perfil do usuário logado
            obj.save()
        else:
            raise ValueError("O usuário logado não possui um perfil Member associado.")

# Registra os modelos no Django Admin
admin.site.register(Member, MemberAdmin)
admin.site.register(Feedback, FeedbackAdmin)
