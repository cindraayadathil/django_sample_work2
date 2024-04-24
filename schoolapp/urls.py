from django.urls import path
from schoolapp.views import *

urlpatterns = [
    path('student/list',student_list,name='student_list'),
    path('school/list',school_list,name='school_list'),
    path('batch/list',batch_list,name='batch_list'),
    path('student/add',student_add,name='student_add'),
    path('school/add',school_add,name='school_add'),
    path('batch/add',batch_add,name='batch_add'),
    path('school/<int:school_id>/view/',school_view,name='school_view'),
    path('batch/<int:batch_id>/view/',batch_view,name='batch_view'),
    path('student/<int:student_id>/view/',student_view,name='student_view'),
    path('school/<int:school_id>/delete/',school_delete,name='school_delete'),
    path('batch/<int:batch_id>/delete/',batch_delete,name='batch_delete'),
    path('student/<int:student_id>/delete/',student_delete,name='student_delete'),
    path('student/<int:student_id>/patch/',student_patch,name='student_patch'),
    path('batch/<int:batch_id>/patch/',batch_patch,name='batch_patch'),
    path('school/<int:school_id>/patch/',school_patch,name='school_patch'),
    path('student/<int:student_id>/put/',student_put,name='student_put'),
    path('school/<int:school_id>/put/',school_put,name='school_put'),
    path('batch/<int:batch_id>/put/',batch_put,name='batch_put'),
    path('school/<int:school_id>/batch/',SchoolWithBatch.as_view(),name='School-With-Batch'),


]