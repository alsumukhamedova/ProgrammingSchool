from django.contrib import admin

from .models import OperatingTime, SystemLoadInformation, CaseParam, TaskParams, ReportSystemLoad, \
    ProcessingResult

admin.site.register(OperatingTime)
admin.site.register(SystemLoadInformation)
admin.site.register(CaseParam)
admin.site.register(TaskParams)
admin.site.register(ReportSystemLoad)
admin.site.register(ProcessingResult)
