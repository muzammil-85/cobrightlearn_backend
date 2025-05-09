from rest_framework import serializers
from .models import CustomUser, Course

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age', 'education_qualification', 'phone_number', 'course', 'role']
        
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            age=validated_data.get('age'),
            education_qualification=validated_data.get('education_qualification'),
            phone_number=validated_data.get('phone_number'),
            course=validated_data.get('course'),
            role=validated_data.get('role', 'student'),
        )
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'education_qualification', 'phone_number', 'course']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
