from rest_framework import serializers
from .models import Member, Feedback

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


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