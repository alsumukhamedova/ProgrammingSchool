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


@api_view(['POST'])
def send_result(request):
    ''' Request for ResultSend
    :param request:
        user_id - personal user id like in database
        task_id - personal task id like in database
        program_language - name of program language to test code
        testing_stage - value in tuple of testing stage
    :return:
        POST: Server gets some data
    '''
    return Response({"message": "Got some data!", "data": request.data})


@api_view(['GET'])
def check_send(request):
    ''' Request for CheckSend
    :return:
        GET:
            solution_status - value in tuple of solution status stage
            task_id - personal task id like in database
            program_language - name of program language to test code
    '''
    checks = CheckSend.objects.all()
    serializer = CheckSendSerializer(checks, many=True)
    return Response({"check": serializer.data})
