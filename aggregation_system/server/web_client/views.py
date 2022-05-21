import os

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CompleteTask, UserTypes, Users, Tasks
from .serializers import CompleteTaskSerializer, StudentGroupInfoSerializer
from .submit import submit_run
import asyncio

FILE_DIR = '/home/gypsyjr-virtual/PycharmProjects/aggregation_system/aggregation_system/server/web_client/files/'


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
    return render(request, 'studentTasks.html',
                  {'tasks': [
                      "123",
                      "345",
                      "456",
                      "123",
                      "345",
                      "456"
                  ]})


def task(request, task_id):
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


def group_statistics(request, task_id):
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


def teacher_tasks(request):
    return render(request, 'teacherTasks.html',
                  {'tasks': [
                      "123",
                      "345",
                      "456",
                      "123",
                      "345",
                      "456"
                  ]})


def teacher_task(request, task_id):
    description = f'Test Task Description for task {task_id}'
    return render(request, 'teacherTaskDescription.html',
                  {'description': description})


def teacher_groups(request, teacher):
    results = CompleteTask.objects.filter(teacher=teacher)
    context = {'group_list': results}

    return render(request, 'teacherGroups.html',
                  context=context)


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
    data = request.data
    path_file = FILE_DIR + data["user_id"] + "_" + data["task_id"] + ".py"

    with open(path_file, "w") as file:
        file.write(data["code"])

    file.close()

    test = asyncio.run(
        submit_run(
            path_file,
            "2",
            "python3",
            data["task_id"],
        )
    )

    os.remove(path_file)
    result = CompleteTask(user_id=get_object_or_404(Users, id=data["user_id"]),
                          task_id=get_object_or_404(Tasks, id=data["task_id"]),
                          program_lang=data["program_lang"], status=test["STATUS"],
                          time=test["TIME"], size=test["SIZE"])

    result.save()

    return Response({"message": "Got some data!", "data": test})


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
    results = CompleteTask.objects.filter(user_id=data["user-id"]).filter(task_id=data["task-id"])
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
        print(form['user-login'])
        user = get_object_or_404(Users, user_login=form['user-login'], user_password=form['user-password'])

    print(user.user_login)
    response = Response()
    response.set_cookie('id', user.id)
    response.set_cookie('login', user.user_login)
    response.set_cookie('mail', user.user_mail)
    response.set_cookie('name', user.user_name)
    response.set_cookie('type', user.user_type)

    return response
