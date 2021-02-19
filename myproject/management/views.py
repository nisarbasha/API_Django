from django.shortcuts import render
from django.http import HttpResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializers, EmployeeUpdateSerializers
from rest_framework.decorators import api_view


# Create your views here
@swagger_auto_schema(methods=['POST'], responses={201: 'RECORD CREATED', 400: 'Bad Request'},
                     request_body=EmployeeSerializers)
@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        serialize_data = EmployeeSerializers(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_201_CREATED)
        return Response(serialize_data.data, status=status.HTTP_400_BAD_REQUEST)




search_record = openapi.Parameter('search_record', openapi.IN_QUERY, type=openapi.TYPE_STRING)
@swagger_auto_schema(methods=['GET'], responses={201: 'RECORD CREATED', 400: 'Bad Request'})
@api_view(['GET'])
def get_employee(request):
    data = Employee.objects.all()
    record = EmployeeSerializers(data, many=True)
    return Response(record.data)


@swagger_auto_schema(methods=['GET'], manual_parameters=[search_record],
                     responses={201: 'RECORD CREATED', 400: 'Bad Request'})
@api_view(['GET'])
def search_employee(request):
    search_records = request.GET.get('search_record', None)
    print(search_records)
    if search_records is not None:
        data = Employee.objects.filter(name=search_records)
        record = EmployeeSerializers(data, many=True)
        return Response(record.data)
    return Response('record not found')

record_id = openapi.Parameter('record_id', openapi.IN_QUERY, type=openapi.TYPE_STRING)
@swagger_auto_schema(methods=['PUT'], manual_parameters=[record_id],
                     responses={201: 'RECORD CREATED', 400: 'Bad Request'})
@api_view(['PUT'])

def update_employee(request):
    record= request.GET.get(name= record_id)
    if record is not None:

        record_data= Employee.objects.get(id=record)
        return Response(record_data)



