from django.contrib import admin
from IQuiriumApp import models
from .models import Convite, Member,Feedback

# Inline para exibir convites na página de detalhes de um Member
class ConviteInline(admin.TabularInline):
    model = Convite
    fields = ['userDestinatario', 'status', 'link', 'data_envio']
    readonly_fields = ['link', 'data_envio']  # Campos de leitura
    extra = 0  # Evita convites extras automaticamente

class ConviteAdmin(admin.ModelAdmin):
    exclude = ('userRemetente', 'link')  # Oculta os campos no Django Admin

    def save_model(self, request, obj, form, change):
        # Define o userRemetente como o usuário logado, se não estiver definido
        if not obj.userRemetente_id:
            obj.userRemetente = request.user.member
        obj.save()

class FeedbackInline(admin.TabularInline):
    model = Feedback
    fields = ['feedback', 'data', 'tipo']
    readonly_fields = ['data']  # Campos de leitura
    extra = 0  # Evita criação automática de novos feedbacks

class FeedbackAdmin(admin.ModelAdmin):
    exclude = ('member',)  # Oculta o campo member no FeedbackAdmin

    def save_model(self, request, obj, form, change):
        if hasattr(request.user, 'member'):
            obj.member = request.user.member  # Define o member como o perfil do usuário logado
            obj.save()
        else:
            raise ValueError("O usuário logado não possui um perfil Member associado.")

class MemberAdmin(admin.ModelAdmin):
    exclude = ('user',)  # Oculta campos específicos
    inlines = [ConviteInline, FeedbackInline]  # Adiciona convites na página de detalhes de um Member

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        obj.save()

# Registra os modelos no Django Admin
admin.site.register(Member, MemberAdmin)
admin.site.register(Convite, ConviteAdmin)
admin.site.register(Feedback, FeedbackAdmin)
