from .models import Student,StudentAttendance
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class AttentenceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentAttendance
        fields =['id', 'is_present', 'date', 'leave_type']