from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    def __str__(self):
        return self.name
        
class Batch(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)
    COURSE=(('MCA','mca'),('MBA','mba'))
    course = models.CharField(max_length=100,choices=COURSE,default=1)
    year = models.IntegerField()
    def __str__(self):
        return self.course


class Student(models.Model):
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    GENDER =(('male','male'),('female','female'),('others','others'))
    gender = models.CharField(max_length=100,choices=GENDER,default=1)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name