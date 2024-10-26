from django.contrib import admin
from member_get_member import models
from .models import Convite

class ConviteAdmin(admin.ModelAdmin):
    # Oculta os campos no Django Admin
    exclude = ('userRemetente','status',)

    def save_model(self, request, obj, form, change):
        # Define o userRemetente como o usuário logado, se não estiver definido
        if not obj.userRemetente_id:
            obj.userRemetente = request.user.member
        obj.save()

# Registra os modelos no Django Admin
admin.site.register(models.Member)
admin.site.register(Convite, ConviteAdmin)
