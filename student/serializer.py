
from rest_framework import serializers
from django.contrib.auth.models import User

# Loal Django Apps
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # user_id = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['name', 'email', 'password', 'age', 'semester', 'user_id', 
                  'enroll_num', 'gender', 'hobbies', 'class_teacher', 'profile_pic']


class UserSerializer(serializers.ModelSerializer):
    # Show id of students
    #  {
    #     "id": 4,
    #     "username": "Mike",
    #     "student": 2
    # }
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    print("----stu--------",student)

    # Show url for detail student page for every  user 
    #  {
    #     "id": 4,
    #     "username": "Mike",
    #     "student": "http://127.0.0.1:8000/studentapi/2/"
    # }
    # student = serializers.HyperlinkedRelatedField( view_name='studentapi-detail', read_only=True)
    # print("----stu--------",student)


    class Meta:
        model = User
        # fields = ['id', 'username']
        fields = ['id', 'username', 'student']