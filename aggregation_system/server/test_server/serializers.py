from rest_framework import serializers
from .models import OperatingTime, SystemLoadInformation, CaseParam, TaskParams, ReportSystemLoad, \
    ProcessingResult


class OperatingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingTime
        fields = ("max_time", "min_time", "average_time")


# class ResourceLoadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ResourceLoad
#         fields = ("cpu", "ram")


class SystemLoadInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemLoadInformation
        # fields = ("max_params", "min_params")
        fields = ("max_cpu", "min_cpu", "max_ram", "min_ram")


class CaseParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseParam
        # fields = ("test_case", "operating_time", "resource_load")
        fields = ("test_case", "max_time", "min_time", "average_time", "resource_load")


class TaskParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskParams
        fields = ("user_id", "task_id", "program_language", "case_params", "solution")


class ReportSystemLoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportSystemLoad
        fields = ("cpu", "ram", "time_spent")


class ProcessingResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessingResult
        fields = ("user_id", "task_id", "program_language", "solution", "result_params")
