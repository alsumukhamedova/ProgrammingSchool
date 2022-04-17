from django.conf.urls.static import static
from django.urls import path

# from .views import ResultSendView, CheckSendView
from .views import send_result, check_send, task, group_statistics


"""Links in web_client app"""

urlpatterns = [
                  path('check/', check_send),
                  path('result/', send_result),
                  path('tasks/<int:task_id>', task, name='task'),
                  path('statistics/<int:task_id>', group_statistics, name='group_statistics')
              ] + static('templates')

