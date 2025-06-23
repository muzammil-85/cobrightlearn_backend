from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from common.mixin import CustomResponseMixin

from .serializers import (
    RegisterSerializer,
    UserListSerializer,
    CourseSerializer,
    PhoneTokenObtainPairSerializer
)
from .models import Course
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from accounts.serializers import RegisterSerializer

User = get_user_model()

class PhoneTokenObtainPairView(TokenObtainPairView):
    serializer_class = PhoneTokenObtainPairSerializer

class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Account successfully registered",
                "err_msg": ""
            }, status=status.HTTP_201_CREATED)
        else:
            # Get first error message
            err_msg = next(iter(serializer.errors.values()))[0]
            return Response({
                "status": False,
                "message": "",
                "err_msg": err_msg
            }, status=status.HTTP_400_BAD_REQUEST)

class StudentListView(CustomResponseMixin, generics.ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(role='student')

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return self.custom_response(data=serializer.data)
        except Exception as e:
            return self.custom_response(success=False, err_msg=str(e), status_code=500)

class TutorListView(CustomResponseMixin, generics.ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(role='tutor')

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return self.custom_response(data=serializer.data)
        except Exception as e:
            return self.custom_response(success=False, err_msg=str(e), status_code=500)


class CourseListView(CustomResponseMixin, viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return self.custom_response(data=serializer.data)
        except Exception as e:
            return self.custom_response(success=False, err_msg=str(e), status_code=500)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return self.custom_response(data=serializer.data)
        except Exception as e:
            return self.custom_response(success=False, err_msg=str(e), status_code=404)
