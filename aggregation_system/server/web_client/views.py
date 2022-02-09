from django.shortcuts import render

from .models import ResultSend, CheckSend
from .serializers import ResultSendSerializer, CheckSendSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST', 'GET'])
def send_result(request):
    ''' Request for ResultSend
    :param request:
        user_id - personal user id like in database
        task_id - personal task id like in database
        program_language - name of program language to test code
        testing_stage - value in tuple of testing stage
    :return:
        GET: base class
        POST: Server gets some data
    '''
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    results = ResultSend.objects.all()
    serializer = ResultSendSerializer(results, many=True)
    return Response({"results": serializer.data})


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
