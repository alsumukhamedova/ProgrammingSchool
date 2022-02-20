from rest_framework import serializers
from .models import ResultSend, CheckSend


class ResultSendSerializer(serializers.ModelSerializer):
    """Serializer for ResultSend class"""
    class Meta:
        model = ResultSend
        fields = '__all__'


class CheckSendSerializer(serializers.ModelSerializer):
    """Serializer for CheckSend class"""
    class Meta:
        model = CheckSend
        fields = '__all__'
