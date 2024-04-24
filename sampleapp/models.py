from django.db import models

# Create your models here.


class Course(models.Model):
    course=models.CharField(max_length=100)

    def __str__(self):
        return self.course 
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    phonenumber = models.CharField(max_length=100)

    def __str__(self):
        return self.name

