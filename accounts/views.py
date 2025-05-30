from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from .serializers import (
    RegisterSerializer,
    UserListSerializer,
    CourseSerializer,
    PhoneTokenObtainPairSerializer
)
from .models import Course
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class PhoneTokenObtainPairView(TokenObtainPairView):
    serializer_class = PhoneTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class StudentListView(generics.ListAPIView):
    queryset = User.objects.filter(role='student')
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

class TutorListView(generics.ListAPIView):
    queryset = User.objects.filter(role='tutor')
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

class CourseListView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
