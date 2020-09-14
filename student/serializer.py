
from rest_framework import serializers

# Loal Django Apps
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['name', 'email', 'password', 'age', 'semester',
                  'enroll_num', 'gender', 'profile_pic']