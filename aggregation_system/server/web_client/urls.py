from django.conf.urls.static import static
from django.urls import path

# from .views import ResultSendView, CheckSendView
from .views import send_result, check_send, task


"""Links in web_client app"""

urlpatterns = [
                  path('check/', send_result),
                  path('result/', check_send),
                  path('tasks/<int:task_id>', task, name='task')
              ] + static('templates')

