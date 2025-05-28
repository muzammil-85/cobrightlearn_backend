from rest_framework import viewsets
from .models import RecordedClass
from .serializers import RecordedClassSerializer
from rest_framework.permissions import IsAuthenticated

class RecordedClassViewSet(viewsets.ModelViewSet):
    queryset = RecordedClass.objects.all()
    serializer_class = RecordedClassSerializer
    permission_classes = [IsAuthenticated]

