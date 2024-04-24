from rest_framework import serializers
from .models import Student
from .models import School
from .models import Batch

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    school_name=serializers.SerializerMethodField()
    class Meta:
        model = Batch
        fields ='__all__'

    def get_school_name(self,obj):
        return obj.school.name if obj.school.name else None
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        