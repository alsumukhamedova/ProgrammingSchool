from django.shortcuts import render

from .models import ResultSend, CheckSend
from .serializers import ResultSendSerializer, CheckSendSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render


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
    ]
    return render(request, 'groupStatistic.html', {
        'task': {'id': task_id, 'name': "Супер сложное задание 1"},
        'person_list': person_list
    })


@api_view(['POST'])
def check_send(request):
    ''' Request for CheckSend
    :param request:
        user_id - personal user id like in database
        task_id - personal task id like in database
        program_language - name of program language to test code
        testing_stage - value in tuple of testing stage
        code - file with the user's code
    :return:
        POST: Server gets some data
    '''

    return Response({"message": "Got some data!", "data": request.data})


@api_view(['GET'])
def send_result(request):
    ''' Request for ResultSend
    :return:
        GET:
            solution_status - value in tuple of solution status stage
            task_id - personal task id like in database
            program_language - name of program language to test code
    '''
    results = ResultSend.objects.all()
    serializer = ResultSendSerializer(results, many=True)
    return Response({"check": serializer.data})
