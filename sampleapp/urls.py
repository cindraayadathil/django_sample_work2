from django.urls import path
from sampleapp.views import *

urlpatterns =[
    path('student',student,name='student'),
    path('student/add',student_add,name='student_add'),
    path('student/<int:student_id>/delete/',student_delete,name='student_delete'),
    path('student/<int:student_id>/view/',student_view,name='student_view'),
    path('student/<int:student_id>/patch/',student_patch,name='student_patch'),
    path('student/<int:student_id>/put/',student_put,name='student_put'),



]