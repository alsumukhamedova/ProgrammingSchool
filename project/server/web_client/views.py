from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .datas import OperatingTime
from .serializers import OperatingTimeSerializer

from collections import namedtuple

nt = namedtuple("object", ["dataclass", "serializers"])
pattern = {
    "operating-time": nt(OperatingTime, OperatingTimeSerializer)
}


@api_view(["GET", "POST"])
def ListView(request, api_name):
    object = pattern.get(api_name, None)
    if object == None:
        return Response(
            data="Invalid URL",
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        object_list = object.dataclass.objects.all()
        serializers = object.serializers(object_list, many=True)
        return Response(serializers.data)

    if request.method == "POST":
        data = request.data
        serializers = object.serializers(data=data)

        if not serializers.is_valid():
            return Response(
                data=serializers.error,
                status=status.HTTP_404_NOT_FOUND
            )
        serializers.save()
        return Response(
            data=serializers.error,
            status=status.HTTP_201_CREATED
        )
