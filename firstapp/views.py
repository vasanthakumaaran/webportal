from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from firstapp.models import Deparments,Employees
from  firstapp.serializers import DepartmentSerializers,EmployeeSerializers

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Deparments.objects.all()
        departments_serializer = DepartmentSerializers(departments,many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    
    elif request.method=='POST':
        department_data=JSONParser().parser(request)
        department_serializer=DepartmentSerializers(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Succesfully!!",safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        department=Deparments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer=DepartmentSerializers(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!",safe=False)
        return JsonResponse("Failed to Update.",safe=False)
    
    elif request.method=='DELETE':
        department=Deparments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully!!",safe=False)
