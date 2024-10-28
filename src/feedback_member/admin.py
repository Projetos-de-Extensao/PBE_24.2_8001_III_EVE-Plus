from django.contrib import admin
from .models import Feedback, Member

class FeedbackAdmin(admin.ModelAdmin):
    # Oculta os campos no Django Admin
    exclude = ('member',)

    def save_model(self, request, obj, form, change):
        # Verifica se o usuário logado tem um perfil Member
        if hasattr(request.user, 'member_profile'):
            # Define o member como o perfil do usuário logado, se não estiver definido
            obj.member = request.user.member_profile
            obj.save()
        else:
            raise ValueError("O usuário logado não possui um perfil Member associado.")

# Registra os modelos no Django Admin
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Member)
