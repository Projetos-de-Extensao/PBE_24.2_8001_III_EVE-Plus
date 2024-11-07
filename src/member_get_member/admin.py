from django.contrib import admin
from member_get_member import models
from .models import Convite, Member

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

class MemberAdmin(admin.ModelAdmin):
    exclude = ('nome', 'user', 'email')  # Oculta campos específicos
    inlines = [ConviteInline]  # Adiciona convites na página de detalhes de um Member

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        obj.nome = obj.nome or obj.user.username
        obj.email = obj.email or obj.user.email
        obj.save()

# Registra os modelos no Django Admin
admin.site.register(Member, MemberAdmin)
admin.site.register(Convite, ConviteAdmin)
