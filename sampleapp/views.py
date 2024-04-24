from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serialzers import *
from rest_framework import status


@api_view(['GET'])
def student(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET','POST'])
def student_add(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#  viewing single student based on id    
@api_view(['GET'])
def student_view(request,student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)

# deleting single student based on id     
@api_view(['GET','DELETE'])
def student_delete(request,student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'GET':
        serializer = StudentSerializer(student,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# patch function where only a necessary fields can be update  
@api_view(['GET','PATCH'])
def student_patch(request,student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'error':'student details not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# put function where all the fields are a necessary to be update  
@api_view(['GET','PUT'])
def student_put(request,student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'error':'student details not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    