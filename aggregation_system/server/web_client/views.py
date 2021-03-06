from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Marks, CompleteTask, UserTypes, Users, Tasks, StudentGroupInfo, GroupComposition, MarkedTasks, \
    CheckSend
from .serializers import CompleteTaskSerializer


def id_to_color(color_id):
    if color_id == 1:
        return "green"
    elif color_id == 2:
        return "orange"
    elif color_id == 3:
        return "red"
    return ''


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'logIn.html')


def register(request):
    groups = StudentGroupInfo.objects.values("id", "group_name")
    context = {
        "groups": []
    }

    for it in groups:
        group = {
            "id": it["id"],
            "name": it["group_name"]
        }
        context["groups"].append(group)
    return render(request, 'registration.html', context)


def reset_password(request):
    return render(request, 'resetPassword.html')


def profile_edit(request):
    user = Users.objects.get(id=request.COOKIES.get("id"))
    return render(
        request,
        'teacherProfielEdit.html' if (request.COOKIES.get("type") == 'teacher') else 'studentProfileEdit.html',
        {'full_name': user.user_name,
         'mail': user.user_mail}
    )


def tasks(request):
    """
        Отрисовывает все задания студента
        :return: возвращает задания в формате словаря: {id: int, name: str, points: int}
        """
    student_id = request.COOKIES.get("id")
    group = GroupComposition.objects.filter(student_id=student_id).values("group_id")[0]

    tasks_st = MarkedTasks.objects.filter(group_id=group["group_id"]).values("id", "task_id")
    tasks_info = Tasks.objects.values("id", "task_name", "difficulty_level_id")
    context = {'tasks': []}
    tasks_con = {}

    for it in tasks_st:
        tasks_con[it["id"]] = it["task_id"]

    for it in tasks_info:
        if it["id"] in tasks_con:
            c = {
                "id": it["id"],
                "name": it["task_name"],
                "checked": 'checked' if CompleteTask.objects.filter(task_id__exact=it["id"],
                                                                    user_id=student_id,
                                                                    status='OK').first() is not None else '',
                "color": id_to_color(it["difficulty_level_id"])
            }
            context["tasks"].append(c)

    return render(request, 'studentTasks.html', context)


def all_tasks(request):
    it = Tasks.objects.values()
    context = {"tasks": []}
    for t in it:
        context["tasks"].append({
            "id": t["id"],
            "name": t["task_name"],
            "difficulty_level_id": get_object_or_404(Marks, id=t["difficulty_level_id"]).mark_description,
            "color": id_to_color(t["difficulty_level_id"])
        })
    return render(request, 'studentAllTasks.html', context)


def task(request, task_id):
    """
        Отрисовывает страницу одного задания по task_id + решение студента (last_solution) + результат (runtime и memory)
        :param task_id: id задания из бд
        :return: возвращает описание задания по task_id, последнее решение, runtime, memory
        """

    it = Tasks.objects.filter(id=task_id).values()[0]
    dif_lvl = Marks.objects.filter(id=it["difficulty_level_id"]).values("mark_description")[0]
    user_id = request.COOKIES.get("id")
    results = CompleteTask.objects.filter(user_id=user_id, task_id=task_id).values()
    try:
        code = CheckSend.objects.filter(user_id=user_id, task_id_id=task_id).values("code")[0]["code"]
    except IndexError:
        code = ""

    context = {
        "id": it["id"],
        "task_name": it["task_name"],
        "task_description": it["task_description"],
        "test_data": it["test_data"],
        "time_to_solve": it["time_to_solve"],
        "resource_load": it["resource_load"],
        "difficulty_level": dif_lvl["mark_description"],
        "last_solution": code,
        "results": [{
            "status": result["status"],
            "time": result["time"],
            "size": result["size"]
        } for result in results]
    }

    return render(request, 'studentTaskDescription.html',
                  context)


def group_statistics(request, task_id, group_id):
    """
    Отрисовывает список студентов с их баллами (с профиля преподавателя) по заданию task_id
    :param group_id: id группы из бд
    :param task_id: id задания из бд
    :return: возвращает список студентов в формате {name: str, score: int}, а также название задания из бд
    """

    teacher_id = request.COOKIES.get("id")
    group = StudentGroupInfo.objects.get(teacher=teacher_id, id=group_id)
    task = Tasks.objects.get(id=task_id)
    person_list = Users.objects.filter(completetask__task_id_id__exact=task_id,
                                       completetask__status__exact='OK').values("user_name").distinct()

    context = {'task': {'id': task.id, 'name': task.task_name},
               'group': {'id': group.id, 'name': group.group_name},
               'person_list': list(person_list)}

    return render(request, 'groupStatistic.html', context)


def students_by_group(request, group_id):
    """
    Отрисовывает список студентов с их баллами (с профиля преподавателя) по группе group_id
    :param group_id: id группы из бд
    :return: возвращает список студентов в формате {name: str, score: int}, а также название группы из бд
    """
    teacher_id = request.COOKIES.get("id")
    group = StudentGroupInfo.objects.get(teacher=teacher_id, id=group_id)
    person_list = Users.objects.filter(groupcomposition__group_id__exact=group_id).values("user_name").distinct()

    context = {'group': {'id': group.id, 'name': group.group_name},
               'person_list': list(person_list)}

    return render(request, 'groupStatistic.html', context)


def teacher_tasks(request):
    """
    отрисовывает все задания в формате {id: int, name: str}
    """

    tasks_all = Tasks.objects.values("id", "task_name", "difficulty_level", "difficulty_level_id")
    context = {"tasks": []}
    for it in tasks_all:
        diff_lvl = get_object_or_404(Marks, id=it["difficulty_level"])
        context["tasks"].append({
            "id": it["id"],
            "name": it["task_name"],
            "difficulty_level": diff_lvl.mark_description,
            "color": id_to_color(it["difficulty_level_id"])
        })

    return render(request, 'teacherTasks.html', context)


def teacher_task(request, task_id):
    """
    Отрисовывает страницу с описанием открытой задачи с профиля преподавателя
    :param task_id: id задачи из бд
    :return: описание задачи
    """
    teacher_id = request.COOKIES.get("id")
    tasks_info = Tasks.objects.get(id=task_id)
    groups = StudentGroupInfo.objects.filter(teacher_id=teacher_id)
    context = {
        'description': tasks_info.task_description,
        'name': tasks_info.task_name,
        "all_groups": [{
            "name": group['group_name'],
            "id": group['id']
        } for group in groups.values()],
        "marked_groups": [{
            "name": group['group_name'],
            "id": group['id']
        } for group in groups.filter(markedtasks__task_id__exact=task_id, teacher_id=teacher_id).values()],
        "task_id": task_id
    }
    return render(request, 'teacherTaskDescription.html', context)


def teacher_groups(request):
    """
    Отрисовывает страницу со списком групп с профиля преподавателя
    :return: возвращает список групп в формате {id: int, name: str}
    """
    teacher_id = request.COOKIES.get("id")
    groups = StudentGroupInfo.objects.filter(teacher_id=teacher_id)

    context = {'group_list': []}

    for group in groups:
        con = {
            "id": group.id,
            "name": group.group_name
        }
        context["group_list"].append(con)

    return render(request, 'teacherGroups.html',
                  context)


@api_view(['POST'])
def check_send(request):
    """ Request for CheckSend
    :param request:
        user_id - personal user id like in database
        task_id - personal task id like in database
        program_lang - name of program language to test code
        code - file with the user's code
    :return:
        data with format...
    """
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(['GET'])
def send_result(request):
    """ Request for ResultSend
     :param request:
        user_id - personal user id like in database
        task_id - personal task id like in database
    :return:
         solution_status - value in tuple of solution status stage
         task_id - personal task id like in database
         program_language - name of program language to test code
    """
    data = request.headers
    user_id = request.COOKIES.get("id")
    results = CompleteTask.objects.filter(user_id=user_id).filter(task_id=data["task-id"]).values()
    context = {"results": []}
    for result in results:
        context["results"].append({
            "status": result["status"],
            "time": result["time"],
            "size": result["size"]
        })

    data = request.headers
    user_id = request.COOKIES.get("id")
    results = CompleteTask.objects.filter(user_id=user_id).filter(task_id=data["task-id"])
    serializer = CompleteTaskSerializer(results, many=True)
    return Response({"check": serializer.data})


@api_view(['POST'])
def sign_up(request):
    """
    Sign up form
    Args:
        user_login - user's login
        user_password - user's password
        user_type - student or teacher
        user_mail - user's mail
        user_name - user's name
        group_name - student's group
    Returns:
            Error or message - 'Got some data!'

    """
    types = list(UserTypes.objects.all())
    print(types)
    if len(types) == 0:
        UserTypes.objects.create(user_type='student')
        UserTypes.objects.create(user_type='teacher')
    form = request.data

    if form['user_type'] == 'student':
        user = Users(user_login=form['user_login'], user_password=form['user_password'],
                     user_type=get_object_or_404(UserTypes, user_type='student'), user_mail=form['user_mail'],
                     user_name=form['user_name'])
        user.save()
        student_group = GroupComposition(group_id=get_object_or_404(StudentGroupInfo, id=form["group_name"]),
                                         student_id=get_object_or_404(Users, user_login=form['user_login']))
        student_group.save()
    else:
        user = Users(user_login=form['user_login'], user_password=form['user_password'],
                     user_type=get_object_or_404(UserTypes, user_type='teacher'), user_mail=form['user_mail'],
                     user_name=form['user_name'])
        user.save()

    return Response({"message": "Got some data!", "data": request.data})


@api_view(['GET'])
def login_user(request):
    """
    Login form
    Args:
        user_login - user's login
        user_mail - user's mail
        user_password - user's password

    Returns:
        Cookies:
            id - user's id
            user_login - user's login
            user_type - student or teacher
            user_mail - user's mail
            user_name - user's name
    """
    form = request.headers
    if 'user-mail' in form:
        user = get_object_or_404(Users, user_mail=form['user-mail'], user_password=form['user-password'])
    else:
        user = get_object_or_404(Users, user_login=form['user-login'], user_password=form['user-password'])

    response = Response()
    response.set_cookie('id', user.id)
    response.set_cookie('login', user.user_login)
    response.set_cookie('mail', user.user_mail)
    response.set_cookie('name', user.user_name)
    response.set_cookie('type', user.user_type)

    return response


@api_view(['POST'])
def teacher_groups_add(request):
    """
        POST:
            Args:
                group_name - name for new group
            Returns:
                    Error or message - 'Got some data!'

        """
    teacher_id = request.COOKIES.get("id")
    data = request.data
    group = StudentGroupInfo(group_name=data["group_name"],
                             teacher=get_object_or_404(Users, id=teacher_id))
    group.save()
    return Response({"message": "Got some data!"})


@api_view(['POST'])
def add_task_group(request):
    """
        POST:
            Args:
                group_id - group's id
                task_id - task's id
            Returns:
                    Error or message - 'Got some data!'
    """
    data = request.data
    marked_tasks = MarkedTasks(group_id=get_object_or_404(StudentGroupInfo, id=data["group_id"]),
                               task_id=get_object_or_404(Tasks, id=data["task_id"]))
    marked_tasks.save()
    return Response({"message": "Got some data!"})


@api_view(['POST'])
def change_info_user(request):
    """
        POST:
            Args:
                user_id - user's id (from cookie)
                user_name - user's name
                user_mail - user's mail
            Returns:
                    Error or message - 'Got some data!'
    """

    user_id = request.COOKIES.get("id")
    data = request.data
    Users.objects.filter(id=user_id).update(user_name=data["user_name"], user_mail=data["user_mail"])

    return Response({"message": "Got some data!"})
