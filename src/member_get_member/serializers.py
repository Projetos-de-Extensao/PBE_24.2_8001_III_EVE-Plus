from rest_framework import serializers
from .models import Member,Convite

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class ConviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convite
        fields = ['userRemetente', 'userDestinatario', 'link', 'status', 'data_envio']
        read_only_fields = ['userRemetente', 'link', 'status', 'data_envio']

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            userRemetente = Member.objects.get(user=request.user)
            validated_data['userRemetente'] = userRemetente
        return Convite.objects.create(**validated_data)