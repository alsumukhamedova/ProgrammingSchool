from django.conf.urls.static import static
from django.urls import path

# from .views import ResultSendView, CheckSendView
from .views import (index, send_result, check_send, tasks, task,
                    teacher_groups, teacher_tasks, teacher_task,
                    login, register, reset_password, profile_edit,
                    sign_up, login_user, students_by_group, teacher_groups_add,
                    add_task_group, change_info_user, all_tasks, group_statistics)

"""Links in web_client app"""

urlpatterns = [
                  path('', index),
                  path('sign-up/', sign_up),
                  path('login-user/', login_user),
                  path('change-info/', change_info_user),

                  path('login/', login),
                  path('register/', register),

                  path('reset_password/', reset_password),

                  path('request/check/', check_send),
                  path('request/result/', send_result),

                  path('profile_edit/', profile_edit),
                  path('tasks/', tasks, name='tasks'),
                  path('tasks/<int:task_id>', task, name='task'),
                  path('tasks/all', all_tasks, name='all_tasks'),

                  path('teacher/groups', teacher_groups, name='teacher_groups'),
                  path('teacher/groups/<int:group_id>', students_by_group, name='students_by_group'),
                  path('teacher/tasks/', teacher_tasks, name='teacher_tasks'),
                  path('teacher/tasks/<int:task_id>', teacher_task, name='teacher_task'),
                  path('teacher/tasks/<int:task_id>/<int:group_id>', group_statistics, name='group_statistics'),
                  path('teacher/add-group', teacher_groups_add, name='teacher_groups_add'),
                  path('teacher/add-task', add_task_group, name='add_task_group'),
              ] + static('templates')
