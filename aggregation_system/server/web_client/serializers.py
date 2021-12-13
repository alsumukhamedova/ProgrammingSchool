from rest_framework import fields, serializers
from .models import ResultSend, CheckSend


class ResultSendSerializer(serializers.ModelSerializer):
    """Serializer for ResultSend class"""
    class Meta:
        model = ResultSend
        fields = ("solution_status", "task_id", "program_lang")


class CheckSendSerializer(serializers.ModelSerializer):
    """Serializer for CheckSend class"""
    class Meta:
        model = CheckSend
        fields = ("user_id", "task_id", "program_lang", "testing_stage")
