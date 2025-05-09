from rest_framework import viewsets
from .models import OnlineClass
from .serializers import OnlineClassSerializer

class OnlineClassViewSet(viewsets.ModelViewSet):
    queryset = OnlineClass.objects.all()
    serializer_class = OnlineClassSerializer
