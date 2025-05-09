from rest_framework import generics,viewsets
from .serializers import RegisterSerializer
from .models import CustomUser
from .serializers import UserListSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Course
from .serializers import CourseSerializer
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class StudentListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role='student')
    serializer_class = UserListSerializer
    # permission_classes = [IsAuthenticated]

class TutorListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role='tutor')
    serializer_class = UserListSerializer
    # permission_classes = [IsAuthenticated]



class CourseListView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer