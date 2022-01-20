from django.shortcuts import render
from .models import OperatingTime, ResourceLoad, SystemLoadInformation, CaseParam, TaskParams, ReportSystemLoad, \
    ProcessingResult
from .serializers import OperatingTimeSerializer, ResourceLoadSerializer, SystemLoadInformationSerializer, \
    CaseParamSerializer, TaskParamsSerializer, ReportSystemLoadSerializer, ProcessingResultSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def operating_time(request):
    results = OperatingTime.objects.all()
    serializer = OperatingTimeSerializer(results, many=True)
    return Response({"results": serializer.data})


@api_view(['GET'])
def resource_load(request):
    results = ResourceLoad.objects.all()
    serializer = ResourceLoadSerializer(results, many=True)
    return Response({"results": serializer.data})


@api_view(['GET'])
def system_load_information(request):
    results = SystemLoadInformation.objects.all()
    serializer = SystemLoadInformationSerializer(results, many=True)
    return Response({"results": serializer.data})


@api_view(['GET'])
def case_param(request):
    results = CaseParam.objects.all()
    serializer = CaseParamSerializer(results, many=True)
    return Response({"results": serializer.data})


@api_view(['GET'])
def task_params(request):
    results = TaskParams.objects.all()
    serializer = TaskParamsSerializer(results, many=True)
    return Response({"results": serializer.data})


@api_view(['GET'])
def report_system_load(request):
    results = ReportSystemLoad.objects.all()
    serializer = ReportSystemLoadSerializer(results, many=True)
    return Response({"results": serializer.data})


@api_view(['GET'])
def processing_result(request):
    results = ProcessingResult.objects.all()
    serializer = ProcessingResultSerializer(results, many=True)
    return Response({"results": serializer.data})
