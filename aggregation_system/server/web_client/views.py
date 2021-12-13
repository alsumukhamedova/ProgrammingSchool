from django.shortcuts import render

from .models import ResultSend, CheckSend
from .serializers import ResultSendSerializer, CheckSendSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ResultSendView(APIView):
    """Get-request for ResultSend class"""
    def get(self, request):
        results = ResultSend.objects.all()
        serializer = ResultSendSerializer(results, many=True)
        return Response({"results": serializer.data})


class CheckSendView(APIView):
    """Get-request for CheckSend class"""
    def get(self, request):
        checks = CheckSend.objects.all()
        serializer = CheckSendSerializer(checks, many=True)
        return Response({"check": serializer.data})
