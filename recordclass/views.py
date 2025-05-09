from rest_framework import viewsets
from .models import RecordedClass
from .serializers import RecordedClassSerializer

class RecordedClassViewSet(viewsets.ModelViewSet):
    queryset = RecordedClass.objects.all()
    serializer_class = RecordedClassSerializer
