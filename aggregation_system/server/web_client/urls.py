from django.conf.urls.static import static
from django.urls import path

# from .views import ResultSendView, CheckSendView
from .views import (send_result, check_send, tasks, task, group_statistics,
                    teacher_groups, teacher_tasks, teacher_task,
                    login, profile_edit, sign_up, login_user)

"""Links in web_client app"""

urlpatterns = [
                  path('registrate/', sign_up),
                  path('login-user/', login_user),

                  path('login/', login),

                  path('request/check/', check_send),
                  path('request/result/', send_result),

                  path('profile_edit/', profile_edit),
                  path('tasks/', tasks, name='tasks'),
                  path('tasks/<int:task_id>', task, name='task'),
                  path('statistics/<int:task_id>', group_statistics, name='group_statistics'),

                  path('teacher/groups', teacher_groups, name='teacher_groups'),
                  path('teacher/tasks/', teacher_tasks, name='teacher_tasks'),
                  path('teacher/tasks/<int:task_id>', teacher_task, name='teacher_task'),
              ] + static('templates')
