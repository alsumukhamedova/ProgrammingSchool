from django.shortcuts import render, get_object_or_404

from .models import ResultSend, CheckSend, UserTypes, Users
from .serializers import ResultSendSerializer, CheckSendSerializer, UsersSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'logIn.html')


def register(request):
    return render(request, 'registration.html')


def reset_password(request):
    return render(request, 'resetPassword.html')


def profile_edit(request):
    # if student, render studentProfileEdit.html
    # if teacher, render teacherProfielEdit.html
    return render(request, 'studentProfileEdit.html')


def tasks(request):
    """
    Отрисовывает все задания студента
    :return: возвращает задания в формате словаря: {id: int, name: str, points: int}
    """
    return render(request, 'studentTasks.html',
                  {'tasks': [
                      {"id": 123, "name": "newTask0", "points": 10},
                      {"id": 234, "name": "newTask1", "points": 7},
                      {"id": 345, "name": "newTask2", "points": 3},
                      {"id": 456, "name": "newTask3", "points": 8}
                  ]})


def task(request, task_id):
    """
    Отрисовывает страницу одного задания по task_id + решение студента (last_solution) + результат (runtime и memory)
    :param task_id: id задания из бд
    :return: возвращает описание задания по task_id, последнее решение, runtime, memory
    """
    # try:
    #     p = Tasks.objects.get(pk=task_id)
    # except Tasks.DoesNotExist:
    #     raise Http404("Task does not exist")
    description = f'Test Task Description for task {task_id}'
    last_solution = 'Last solution written'
    runtime = 0  # last runtime
    memory = 0  # last memory
    runtime = f'{runtime} ms'
    memory = f'{memory} Mb'
    return render(request, 'studentTaskDescription.html',
                  {'description': description, 'last_solution': last_solution,
                   'runtime': runtime, 'memory': memory})


def students_by_task(request, task_id):
    """
    Отрисовывает список студентов с их баллами (с профиля преподавателя) по заданию task_id
    :param task_id: id задания из бд
    :return: возвращает список студентов в формате {name: str, score: int}, а также название задания из бд
    """
    # try:
    #     p = Tasks.objects.get(pk=task_id)
    # except Tasks.DoesNotExist:
    #     raise Http404("Task does not exist")
    person_list = [
        {'name': 'Литвинов Вячевлав', 'score': 0},
        {'name': 'Никоненко Андрей роцкер', 'score': 666},
        {'name': 'Демидов Иван', 'score': 220},
        {'name': 'Бурмистров Владимир', 'score': 5000},
        {'name': 'Мухамедова Алсу', 'score': 404},
        {'name': 'Мухамедова Алсу', 'score': 404},
        {'name': 'Литвинов Вячевлав', 'score': 0},
        {'name': 'Никоненко Андрей роцкер', 'score': 666},
        {'name': 'Демидов Иван', 'score': 220},
        {'name': 'Бурмистров Владимир', 'score': 5000},
        {'name': 'Мухамедова Алсу', 'score': 404},
        {'name': 'Мухамедова Алсу', 'score': 404},
    ]
    return render(request, 'groupStatistic.html', {
        'task': {'id': task_id, 'name': "Супер сложное задание 1"},
        'person_list': person_list
    })


def students_by_group(request, group_id):
    """
    Отрисовывает список студентов с их баллами (с профиля преподавателя) по группе group_id
    :param group_id: id группы из бд
    :return: возвращает список студентов в формате {name: str, score: int}, а также название группы из бд
    """
    # try: В ЭТОЙ ФУНКЦИИ НЕТ ТАСКС, ТОЛЬКО ГРУППЫ
    #     p = Tasks.objects.get(pk=task_id)
    # except Tasks.DoesNotExist:
    #     raise Http404("Task does not exist")
    person_list = [
        {'name': 'Литвинов Вячевлав', 'score': 0},
        {'name': 'Никоненко Андрей роцкер', 'score': 666},
        {'name': 'Демидов Иван', 'score': 220},
        {'name': 'Бурмистров Владимир', 'score': 5000},
        {'name': 'Мухамедова Алсу', 'score': 404},
        {'name': 'Мухамедова Алсу', 'score': 404},
        {'name': 'Литвинов Вячевлав', 'score': 0},
        {'name': 'Никоненко Андрей роцкер', 'score': 666},
        {'name': 'Демидов Иван', 'score': 220},
        {'name': 'Бурмистров Владимир', 'score': 5000},
        {'name': 'Мухамедова Алсу', 'score': 404},
        {'name': 'Мухамедова Алсу', 'score': 404},
    ]
    return render(request, 'groupStatistic.html', {
        'disable_task_descr': True,  # оставить True, не трогать
        'task': {'name': "БИВ190"},  # оставить название "task", менять name
        'person_list': person_list
    })


def teacher_tasks(request):
    """
    отрисовывает все задания с профиля преподавателя в формате {id: int, name: str}
    """
    return render(request, 'teacherTasks.html',
                  {'tasks': [
                      {"id": 123, "name": "newTask0"},
                      {"id": 234, "name": "newTask1"},
                      {"id": 345, "name": "newTask2"},
                      {"id": 456, "name": "newTask3"},
                      {"id": 567, "name": "newTask4"},
                  ]})


def teacher_task(request, task_id):
    """
    Отрисовывает страницу с описанием открытой задачи с профиля преподавателя
    :param task_id: id задачи из бд
    :return: описание задачи
    """
    description = f'Test Task Description for task {task_id}'
    return render(request, 'teacherTaskDescription.html',
                  {'description': description})


def teacher_groups(request):
    """
    Отрисовывает страницу со списком групп с профиля преподавателя
    :return: возвращает список групп в формате {id: int, name: str}
    """
    return render(request, 'teacherGroups.html',
                  {'group_list': [
                      {"id": 123, "name": "group1"},
                      {"id": 234, "name": "group2"},
                      {"id": 345, "name": "group3"},
                      {"id": 456, "name": "group4"},
                  ]})


@api_view(['POST'])
def check_send(request):
    """ Request for CheckSend
    :param request:
        user_id - personal user id like in database
        task_id - personal task id like in database
        program_language - name of program language to test code
        testing_stage - value in tuple of testing stage
        code - file with the user's code
    :return:
        POST: Server gets some data
    """

    return Response({"message": "Got some data!", "data": request.data})


@api_view(['GET'])
def send_result(request):
    """ Request for ResultSend
    :return:
         solution_status - value in tuple of solution status stage
         task_id - personal task id like in database
         program_language - name of program language to test code
    """
    results = ResultSend.objects.all()
    serializer = ResultSendSerializer(results, many=True)
    return Response({"check": serializer.data})


@api_view(['POST'])
def sign_up(request):
    """
    Sign up form
    Args:
        user_login - user's login
        user_password - user's password
        user_type - student or teacher

    Returns:
            Error or message - 'Got some data!'

    """
    types = list(UserTypes.objects.all())
    print(types)
    if len(types) == 0:
        UserTypes.objects.create(user_type='student')
        UserTypes.objects.create(user_type='teacher')
    form = request.data

    if form['user-type'] == 'student':
        user = Users(user_login=form['user-login'], user_password=form['user-password'],
                     user_type=get_object_or_404(UserTypes, user_type='student'))
    else:
        user = Users(user_login=form['user-login'], user_password=form['user-password'],
                     user_type=get_object_or_404(UserTypes, user_type='teacher'))

    user.save()
    return Response({"message": "Got some data!", "data": request.data})


@api_view(['GET'])
def login_user(request):
    """
    Login form
    Args:
        user_login - user's login
        user_password - user's password

    Returns:
        User:
            id - user's id
            user_login - user's login
            user_type - '1' is a student or '2' is a teacher
    """
    form = request.headers
    user = get_object_or_404(Users, user_login=form['user-login'], user_password=form['user-password'])
    serializer = UsersSerializer(user, many=False)
    return Response({"user": serializer.data})
