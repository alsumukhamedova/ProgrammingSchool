from rest_framework_dataclasses.serializers import DataclassSerializer
from .datas import OperatingTime, ResourceLoad, SystemLoadInformation, CaseParam, TaskParams, ReportSystemLoad, \
    ProcessingResult


class OperatingTimeSerializer(DataclassSerializer):
    class Meta:
        dataclass = OperatingTime


class ResourceLoadSerializer(DataclassSerializer):
    class Meta:
        dataclass = ResourceLoad


class SystemLoadInformationSerializer(DataclassSerializer):
    class Meta:
        dataclass = SystemLoadInformation


class CaseParamSerializer(DataclassSerializer):
    class Meta:
        dataclass = CaseParam


class TaskParamsSerializer(DataclassSerializer):
    class Meta:
        dataclass = TaskParams


class ReportSystemLoadSerializer(DataclassSerializer):
    class Meta:
        dataclass = ReportSystemLoad


class ProcessingResultSerializer(DataclassSerializer):
    class Meta:
        dataclass = ProcessingResult
