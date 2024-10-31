from rest_framework import serializers
from .models import Member,Convite

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class ConviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convite
        fields = '__all__'