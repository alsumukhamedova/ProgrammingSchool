from django.urls import path

from .views import operating_time, system_load_information, case_param, task_params, report_system_load, \
    processing_result


"""Links in web_client app"""

urlpatterns = [
    path('operating-time/', operating_time),
    path('system-load-information/', system_load_information),
    path('case-param/', case_param),
    path('task-params/', task_params),
    path('report-system-load/', report_system_load),
    path('processing-result/', processing_result)
]
