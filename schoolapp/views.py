from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .models import *
from .serialzers import *
from rest_framework import status

# list the tables separtely
@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET'])
def school_list(request):
    if request.method == 'GET':
        student = School.objects.all()
        serializer = SchoolSerializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET'])
def batch_list(request):
    if request.method == 'GET':
        student = Batch.objects.all()
        serializer = BatchSerializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
# post the contents seprately
@api_view(['GET','POST'])
def student_add(request):
    if request.method == 'GET':
        student =Student .objects.all()
        serializer = StudentSerializer(student,many=True,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def school_add(request):
    if request.method == 'GET':
        school =School .objects.all()
        serializer = SchoolSerializer(school,many=True,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def batch_add(request):
    if request.method == 'GET':
        batch =Batch.objects.all()
        serializer = BatchSerializer(batch,many=True,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# to view based on id of single category
@api_view(['GET'])
def student_view(request,student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET'])
def batch_view(request,batch_id):
    batch = Batch.objects.get(id=batch_id)
    if request.method == 'GET':
        serializer = BatchSerializer(batch)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET'])
def school_view(request,school_id):
    school = School.objects.get(id=school_id)
    if request.method == 'GET':
        serializer = SchoolSerializer(school)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
  # to delete the content
@api_view(['GET','DELETE'])
def student_delete(request,student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'GET':
        serializer = StudentSerializer(student,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','DELETE'])
def school_delete(request,school_id):
    school = School.objects.get(id=school_id)
    if request.method == 'GET':
        serializer = SchoolSerializer(school,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','DELETE'])
def batch_delete(request,batch_id):
    batch = Batch.objects.get(id=batch_id)
    if request.method == 'GET':
        serializer = BatchSerializer(batch,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        batch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# patch operations 
@api_view(['GET','PATCH'])
def student_patch(request,student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'error':'Category not found'},status=status.HTTP_404_NOT_FOUND)
    
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
    
@api_view(['GET','PATCH'])
def batch_patch(request,batch_id):
    try:
        batch = Batch.objects.get(id=batch_id)
    except Batch.DoesNotExist:
        return Response({'error':'Category not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BatchSerializer(batch,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = BatchSerializer(batch,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PATCH'])
def school_patch(request,school_id):
    try:
        school = School.objects.get(id=school_id)
    except School.DoesNotExist:
        return Response({'error':'Category not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SchoolSerializer(school,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = SchoolSerializer(school,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#PUT OPERATION
@api_view(['GET','PUT'])
def student_put(request,student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'error':'Category not found'},status=status.HTTP_404_NOT_FOUND)
    
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
    
@api_view(['GET','PUT'])
def school_put(request,school_id):
    try:
        school = School.objects.get(id=school_id)
    except School.DoesNotExist:
        return Response({'error':'Category not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SchoolSerializer(school,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SchoolSerializer(school,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def batch_put(request,batch_id):
    try:
        batch = Batch.objects.get(id=batch_id)
    except Batch.DoesNotExist:
        return Response({'error':'Category not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BatchSerializer(batch,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = BatchSerializer(batch,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class SchoolWithBatch(APIView):
    def get(self, request, school_id, format=None):
        try:
            school = School.objects.get(id=school_id)
        except School.DoesNotExist:
            return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)
        
        school_serializer = SchoolSerializer(school)
        batches = Batch.objects.filter(school=school)
        final_data = []
        
        for batch in batches:
            batch_serializer = BatchSerializer(batch)
            students = Student.objects.filter(batch=batch)
            student_serializer = StudentSerializer(students, many=True)
            
            final_data.append({
                'batch': batch_serializer.data,
                'students': student_serializer.data,
            })
        
        response_data = {
            'school': school_serializer.data,
            'batches_with_students': final_data,
        }

        return Response(response_data, status=status.HTTP_200_OK)