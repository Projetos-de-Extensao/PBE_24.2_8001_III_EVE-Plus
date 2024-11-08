from rest_framework import serializers
from .models import Member,Convite,Feedback

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
    
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['member', 'feedback', 'tipo', 'data']
        read_only_fields = ['member','data']

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            user = request.user
            try:
                member = Member.objects.get(user=user)
            except Member.DoesNotExist:
                member = Member.objects.create(user=user)
            validated_data['member'] = member
        return Feedback.objects.create(**validated_data)