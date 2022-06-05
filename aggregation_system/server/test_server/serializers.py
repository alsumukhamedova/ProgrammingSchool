from rest_framework import serializers
from .models import OperatingTime, SystemLoadInformation, CaseParam, TaskParams, ReportSystemLoad, \
    ProcessingResult


class OperatingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingTime
        fields = '__all__'


# class ResourceLoadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ResourceLoad
#         fields = ("cpu", "ram")


class SystemLoadInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemLoadInformation
        # fields = ("max_params", "min_params")
        fields = '__all__'


class CaseParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseParam
        # fields = ("test_case", "operating_time", "resource_load")
        fields = '__all__'


class TaskParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskParams
        fields = '__all__'


class ReportSystemLoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportSystemLoad
        fields = '__all__'


class ProcessingResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessingResult
        fields = '__all__'
