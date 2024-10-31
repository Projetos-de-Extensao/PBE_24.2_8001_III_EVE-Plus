from django.contrib import admin
from member_get_member import models
from .models import Convite, Member

class ConviteAdmin(admin.ModelAdmin):
    # Oculta os campos no Django Admin
    exclude = ('userRemetente','link')

    def save_model(self, request, obj, form, change):
        # Define o userRemetente como o usuário logado, se não estiver definido
        if not obj.userRemetente_id:
            obj.userRemetente = request.user.member
        obj.save()

class MemberAdmin(admin.ModelAdmin):
    # Oculta os campos no Django Admin
    exclude = ('nome','user','email')
    # Define o usuário como o usuário logado, se não estiver definido
    def save_model(self, request, obj, form, change):
        # Define o usuário como o usuário logado, se não estiver definido
        if not obj.user_id:
            obj.user = request.user
        obj.save()

        if not obj.nome:
            obj.nome = obj.user.username
        obj.save()

        if not obj.email:
            obj.email = obj.user.email
        obj.save()


# Registra os modelos no Django Admin
admin.site.register(Member,MemberAdmin)
admin.site.register(Convite, ConviteAdmin)
